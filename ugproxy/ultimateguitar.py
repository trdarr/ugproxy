import html.parser
import json
import re
from urllib.request import urlopen


CHORD_RE = re.compile(r'\[ch\]([^\[]+)\[/ch\]')


class HTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()

        self.done = False
        self.in_body = False
        self.in_script = False

    def handle_starttag(self, tag, attrs):
        self.in_body = self.in_body or tag == 'body'
        self.in_script = self.in_body and tag == 'script'

    def handle_data(self, data):
        if self.done or not self.in_script:
            return

        start, end = data.index('{'), data.rindex('}')
        self.data = json.loads(data[start : end+1])

        self.done = True


def get_tab(url):
    with urlopen(url, timeout=2) as response:
        body = response.read().decode('utf-8')

    parser = HTMLParser()
    parser.feed(body)
    data = parser.data

    metadata = data['data']['tab']
    content = data['data']['tab_view']['wiki_tab']['content']
    return metadata, CHORD_RE.sub(r'\1', content)

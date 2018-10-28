from ugproxy.ultimateguitar import get_tab
from ugproxy.server import create_server


address = ('0.0.0.0', 8000)
create_server(address).serve_forever()

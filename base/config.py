# may be stored in environment variables of a pipeline
from urllib.parse import urljoin

BASE_URL = "https://hb-eta.stage.sirenltd.dev"
HB_SIDING_URL = urljoin(BASE_URL, 'siding')
CHROME_OPTIONS = ("headless",)
# CHROME_OPTIONS = ()

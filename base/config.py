# эти вещи можно хранить в переменных окружения пайплайнов

from urllib.parse import urljoin


BASE_URL = "https://hb-eta.stage.sirenltd.dev"

HB_SIDING_URL = urljoin(BASE_URL, 'siding')

CHROME_OPTIONS = ("disable-infobars", "headless")
# CHROME_OPTIONS = ("disable-infobars")

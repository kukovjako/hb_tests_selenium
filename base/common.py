from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from base.config import CHROME_OPTIONS


def setup_chrome():
    chrome_options = Options()
    for opt in CHROME_OPTIONS:
        chrome_options.add_argument(opt)
    return webdriver.Chrome(options=chrome_options)

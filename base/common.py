import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from base.config import CHROME_OPTIONS
from tests.frontend.constants import PHONE_NUMBER


def setup_chrome():
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if CHROME_OPTIONS:
        for opt in CHROME_OPTIONS:
            chrome_options.add_argument(opt)
    return webdriver.Chrome(options=chrome_options)


def generate_phone_number() -> str:
    # generates random phone number with 555 code
    numbers = []
    for i in range(0, 7):
        numbers.append(random.randint(0, 9))
    first = "".join(str(n) for n in numbers[:3])
    second = "".join(str(n) for n in numbers[3:7])
    return PHONE_NUMBER.format(first, second)

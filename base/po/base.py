import allure
from allure import attachment_type
from webium import BasePage

from base.common import setup_chrome


class HomeBuddyBasePage(BasePage):
    TIMEOUT = 30
    SLEEP_SECONDS = 0.5

    def __init__(self, url):
        self.__driver = setup_chrome()

        self.output_directory = None
        BasePage.__init__(self, self.__driver, url)

    def get_driver(self):
        return self.__driver

    def go_back(self):
        self.__driver.back()

    def get_current_url(self):
        return self.__driver.current_url

    @classmethod
    def screen_after_step(cls, func):
        def wrapper(self, *args, **kwargs):
            func_result = func(self, *args, **kwargs)
            try:
                allure.attach(
                    self.get_screenshot(),
                    name='screenshot_after_step',
                    attachment_type=attachment_type.PNG)
            except Exception as e:
                print("Could`t take screenshot after step: %s" % e)
            return func_result
        return wrapper

    def get_screenshot(self):
        return self.__driver.get_screenshot_as_png()


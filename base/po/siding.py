import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from waiting import wait
from webium import Find

from webium.wait import wait

from base.config import HB_SIDING_URL
from base.po.base import HomeBuddyBasePage


class Header(WebElement):
    no_matching_contractors_title = Find(
        by=By.XPATH,
        value="//h4[contains(text(), 'Unfortunately')]",
        context=WebElement
    )
    unknown_zip_code_alert = Find(
        by=By.XPATH,
        value="//div[contains(text(), 'Unknown ZIP Code')]",
        context=WebElement
    )
    enter_zip_code_alert = Find(
        by=By.XPATH,
        value="//div[contains(text(), 'Enter your ZIP Code')]",
        context=WebElement
    )

    zip_input = Find(
        by=By.CSS_SELECTOR,
        value="input[data-autotest-input-0]",
        context=WebElement
    )
    submit_button = Find(
        by=By.CSS_SELECTOR,
        value="button[data-autotest-button-submit-0]",
        context=WebElement
    )
    right_icon = Find(
        by=By.CLASS_NAME,
        value="rightIcon",
        context=WebElement
    )


class HomeBuddySidingMainPage(HomeBuddyBasePage):
    header = Find(Header, by=By.CSS_SELECTOR, value=".header__content")

    def __init__(self):
        super(HomeBuddySidingMainPage, self).__init__(url=HB_SIDING_URL)

    @allure.step("Open HomeBuddy siding page")
    @HomeBuddyBasePage.screen_after_step
    def open(self):
        super(HomeBuddySidingMainPage, self).open()

    @allure.step("Input zip")
    @HomeBuddyBasePage.screen_after_step
    def input_zip(self, zip_text: str):
        wait(lambda: self.header.is_element_present("zip_input"),
             sleep_seconds=0.5,
             waiting_for="zip input field is present",
             timeout_seconds=self.TIMEOUT)
        self.header.zip_input.send_keys(zip_text)

    @allure.step("Submit zip")
    @HomeBuddyBasePage.screen_after_step
    def submit_zip(self):
        self.header.submit_button.click()
        self.wait_page_loading()

    @allure.step("Waiting for the page to load")
    @HomeBuddyBasePage.screen_after_step
    def wait_page_loading(self):
        wait(lambda: self.get_driver().execute_script("return document.readyState"),
             timeout_seconds=self.TIMEOUT,
             sleep_seconds=1,
             waiting_for="document.readyState returned True")

import allure
import pytest

from webium.wait import wait
from base.po.siding import HomeBuddySidingMainPage


@pytest.fixture
def setup():
    siding_page = HomeBuddySidingMainPage()
    if siding_page.get_driver().current_url != siding_page.url:
        siding_page.open()
        siding_page.wait_page_loading()
    return siding_page


@allure.suite('Siding Main Page')
@allure.feature("Insert testcase Url")
class TestSidingMainPage:
    @allure.story('Siding Main Page header check')
    def test_main_page_header(self, setup):
        """
        1. Открыть главную siding
        2. Проверить наличие header на главной siding
        """
        main_page = setup

        wait(lambda: main_page.is_element_present("header"),
             sleep_seconds=0.5,
             waiting_for="Submit button is present",
             timeout_seconds=main_page.TIMEOUT)

    @allure.story('Siding Main Page no contractors on zip')
    def test_main_page_no_contractors_zip(self, setup):
        """
        1. Открыть siding
        2. Проверить no contractors
        """
        main_page = setup
        main_page.input_zip("90909")
        wait(lambda: main_page.header.is_element_present("right_icon"), sleep_seconds=0.5,
             waiting_for="Right zip icon appeared", timeout_seconds=main_page.TIMEOUT)

        main_page.submit_zip()
        wait(lambda: main_page.header.is_element_present("no_matching_contractors_title"),
             sleep_seconds=0.5,
             waiting_for="'No matching contractors' title is present",
             timeout_seconds=main_page.TIMEOUT)

    @allure.story('Siding Main Page wrong zip')
    @pytest.mark.parametrize("zip_code", [1, "xxxxx", 000000, "./"])
    def test_main_page_wrong_zip(self, setup, zip_code):
        """
        1. Открыть /siding
        2. Проверить wrong zip input
        """
        main_page = setup
        main_page.input_zip(zip_code)
        main_page.submit_zip()
        wait(lambda: main_page.header.is_element_present("unknown_zip_code_alert"),
             sleep_seconds=0.5,
             waiting_for="'Unknown ZIP Code' alert is present",
             timeout_seconds=main_page.TIMEOUT)

    @allure.story('Siding Main Page no zip')
    def test_main_page_no_zip(self, setup):
        """
        1. Открыть /siding
        2. Проверить no zip input
        """
        main_page = setup
        main_page.input_zip("")
        main_page.submit_zip()
        wait(lambda: main_page.header.is_element_present("enter_zip_code_alert"),
             sleep_seconds=0.5,
             waiting_for="'Enter ZIP Code' alert is present",
             timeout_seconds=main_page.TIMEOUT)

import allure
import pytest

from webium.wait import wait
from base.po.page_object import HomeBuddySidingMainPage


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
    @allure.story('Siding Main Page smoke check')
    def test_main_page_smoke(self, setup):
        """
        1. Open Siding landing page
        2. Check for header present on page
        3. Check for "I'm a contractor" link explicitly as it is crucial for business process
        4. Check for the rest of page elements present
        5. Check for 'According to Remodeling' in case it's crucial
        """
        main_page = setup

        wait(lambda: main_page.is_element_present("header"),
             sleep_seconds=0.5,
             waiting_for="Header is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.header.is_element_present("i_am_contractor_link"),
             sleep_seconds=0.5,
             waiting_for="'I'm a contractor' link is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("siding_for_your_home_block"),
             sleep_seconds=0.5,
             waiting_for="'Siding For Your Home' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("siding_types_block"),
             sleep_seconds=0.5,
             waiting_for="'Types Of Siding Projects' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: len(main_page.advantages_of_new_siding_block.advantages_elements) == 6,
             waiting_for="6 advantages of new siding are present", timeout_seconds=10)
        wait(lambda: main_page.is_element_present("if_need_new_siding"),
             sleep_seconds=0.5,
             waiting_for="'How To Know If You Need New Siding' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("home_seem_brand_new_block"),
             sleep_seconds=0.5,
             waiting_for="'Siding Makes Your Home Seem Brand New' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("middle_zip_block"),
             sleep_seconds=0.5,
             waiting_for="Middle zip block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("how_it_works_block"),
             sleep_seconds=0.5,
             waiting_for="'How it works' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("trust_us_block"),
             sleep_seconds=0.5,
             waiting_for="'Trust Us' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("reviews_block"),
             sleep_seconds=0.5,
             waiting_for="'Reviews' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("bottom_zip_block"),
             sleep_seconds=0.5,
             waiting_for="Bottom 'What is your ZIP Code' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("footer"),
             sleep_seconds=0.5,
             waiting_for="Footer is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("according_link"),
             sleep_seconds=0.5,
             waiting_for="'According to Remodeling' link is present",
             timeout_seconds=main_page.TIMEOUT)

    @allure.story('Siding Main Page no contractors on zip')
    def test_main_page_no_contractors(self, setup):
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

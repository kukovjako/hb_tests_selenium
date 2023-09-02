import allure
import pytest

from webium.wait import wait
from base.po.page_object import HomeBuddySidingMainPage
from tests.frontend.constants import \
    SIDING_ZIP_WRONG, SIDING_ZIP_EMPTY, SIDING_ZIP_POSITIVE, SIDING_ZIP_NO_CONTRACTORS, \
    SIDING_AREA_FT, FULL_NAME, EMAIL


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
             waiting_for="Header is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.header.is_element_present("i_am_contractor_link"),
             waiting_for="'I'm a contractor' link is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("siding_for_your_home_block"),

             waiting_for="'Siding For Your Home' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("siding_types_block"),

             waiting_for="'Types Of Siding Projects' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: len(main_page.advantages_of_new_siding_block.advantages_elements) == 6,
             waiting_for="6 advantages of new siding are present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("if_need_new_siding"),

             waiting_for="'How To Know If You Need New Siding' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("home_seem_brand_new_block"),
             waiting_for="'Siding Makes Your Home Seem Brand New' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("middle_zip_block"),
             waiting_for="Middle zip block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("how_it_works_block"),
             waiting_for="'How it works' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("trust_us_block"),
             waiting_for="'Trust Us' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("reviews_block"),
             waiting_for="'Reviews' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("bottom_zip_block"),
             waiting_for="Bottom 'What is your ZIP Code' block is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("footer"),

             waiting_for="Footer is present",
             timeout_seconds=main_page.TIMEOUT)
        wait(lambda: main_page.is_element_present("according_link"),
             waiting_for="'According to Remodeling' link is present",
             timeout_seconds=main_page.TIMEOUT)

    @allure.story('Siding Main Page no contractors on zip')
    def test_main_page_no_contractors(self, setup):
        """
        1. Открыть siding
        2. Проверить no contractors
        """
        main_page = setup
        main_page.input_zip(SIDING_ZIP_NO_CONTRACTORS)
        wait(lambda: main_page.header.is_element_present("right_icon"),
             waiting_for="Right zip icon appeared", timeout_seconds=main_page.TIMEOUT)

        main_page.submit_click()
        wait(lambda: main_page.header.is_element_present("no_matching_contractors_title"),
             waiting_for="'No matching contractors' title is present",
             timeout_seconds=main_page.TIMEOUT)

    @allure.story('Siding Main Page wrong zip')
    @pytest.mark.parametrize("zip_code", SIDING_ZIP_WRONG)
    def test_main_page_wrong_zip(self, setup, zip_code):
        """
        1. Открыть /siding
        2. Проверить wrong zip input
        """
        main_page = setup
        main_page.input_zip(zip_code)
        main_page.submit_click()
        wait(lambda: main_page.header.is_element_present("unknown_zip_code_alert"),
             waiting_for="'Unknown ZIP Code' alert is present",
             timeout_seconds=main_page.TIMEOUT)

    @allure.story('Siding Main Page no zip')
    def test_main_page_no_zip(self, setup):
        """
        1. Открыть /siding
        2. Проверить no zip input
        """
        main_page = setup
        main_page.input_zip(SIDING_ZIP_EMPTY)
        main_page.submit_click()
        wait(lambda: main_page.header.is_element_present("enter_zip_code_alert"),
             waiting_for="'Enter ZIP Code' alert is present",
             timeout_seconds=main_page.TIMEOUT)


@allure.suite('Siding Page positive scenario')
@allure.feature("http://Insert testcase Url")
class TestSidingScenarioPositive:
    @allure.story('Siding Main Page positive scenario')
    def test_siding_scenario_positive(self, setup):
        main_page = setup
        main_page.input_zip(SIDING_ZIP_POSITIVE)
        main_page.submit_click()
        wait(lambda: main_page.is_element_present("questions_form"),
             waiting_for="Questions form is present",
             timeout_seconds=main_page.TIMEOUT)
        main_page.choose_type_of_project()
        main_page.submit_click()
        main_page.choose_type_of_siding()
        main_page.submit_click()
        wait(lambda: main_page.questions_form.is_element_present("how_large_input_block"),
             waiting_for="'How many square feet' block is present",
             timeout_seconds=main_page.TIMEOUT)
        main_page.input_siding_area(SIDING_AREA_FT)
        main_page.submit_click()
        main_page.choose_how_many_stories()
        main_page.submit_click()
        main_page.choose_homeowner_yes()
        main_page.submit_click()
        main_page.input_fullname_email(FULL_NAME, EMAIL)
        main_page.submit_click()
        main_page.input_phone_number()
        main_page.submit_click()
        main_page.confirm_phone()
        wait(lambda: main_page.questions_form.is_element_present("success_message"),
             waiting_for="Phone confirmation request is present",
             timeout_seconds=main_page.TIMEOUT)

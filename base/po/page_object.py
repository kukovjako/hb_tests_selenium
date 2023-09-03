import allure

from selenium.webdriver.common.by import By
from waiting import wait
from webium import Find
from webium.controls.link import Link

from base.common import generate_phone_number
from base.config import HB_SIDING_URL
from base.po.base import HomeBuddyBasePage
from base.po.elements import Header, SidingForYourHomeBlock, SidingTypesBlock, \
    AdvantagesOfNewSidingBlock, SidingPhotoGallery, IfNeedNewSidingBlock, HomeSeemBrandNewBlock, \
    MiddleZipBlock, HowItWorksBlock, TrustUsBlock, ReviewsBlock, BottomZipBlock, Footer, \
    QuestionsFormBlock


class HomeBuddySidingMainPage(HomeBuddyBasePage):
    header = Find(Header, by=By.CLASS_NAME, value="header")
    submit_button = Find(
        by=By.XPATH,
        value="//button[@type='submit']"
    )
    submit_processing = Find(
        by=By.XPATH,
        value="//button[@type='submit' and @data-state='processing']"
    )
    siding_for_your_home_block = Find(
        SidingForYourHomeBlock,
        #  The name of this class was not obvious, so I used XPATH
        by=By.XPATH,
        value="//h3[contains(text(), 'Siding For Your Home')]/ancestor::div/ancestor::section"
    )
    siding_types_block = Find(
        SidingTypesBlock,
        by=By.CLASS_NAME,
        value="typesOfSiding"
    )
    advantages_of_new_siding_block = Find(
        AdvantagesOfNewSidingBlock,
        by=By.CLASS_NAME,
        value="advantages"
    )
    siding_photo_gallery = Find(
        SidingPhotoGallery,
        by=By.CLASS_NAME,
        value="photoGallery"
    )
    if_need_new_siding = Find(
        IfNeedNewSidingBlock,
        by=By.XPATH,
        value="//h3[contains(text(), "
              # Using special symbol for &nbsp; otherwise selector doesn't work
              "'How To Know If You Need New Siding')]/ancestor::div/ancestor::section"
    )
    home_seem_brand_new_block = Find(
        HomeSeemBrandNewBlock,
        by=By.XPATH,
        value="//h3[contains(text(), "
              # Using special symbol for &nbsp; otherwise selector doesn't work
              "'Siding Makes Your Home Seem Brand New')]/ancestor::div/ancestor::section"
    )
    middle_zip_block = Find(
        MiddleZipBlock,
        by=By.CLASS_NAME,
        value="contentZip--middleZip"
    )
    how_it_works_block = Find(
        HowItWorksBlock,
        by=By.CLASS_NAME,
        value="howItWorks"
    )
    trust_us_block = Find(
        TrustUsBlock,
        by=By.CLASS_NAME,
        value="trustUs"
    )
    reviews_block = Find(
        ReviewsBlock,
        by=By.CLASS_NAME,
        value="reviews"
    )
    bottom_zip_block = Find(
        BottomZipBlock,
        by=By.XPATH,
        value="//form[@id='zip_footer']/ancestor::div/ancestor::div"
    )
    footer = Find(
        Footer,
        by=By.CLASS_NAME,
        value="footer"
    )
    according_link = Find(
        Link,
        by=By.XPATH,
        value="//li[contains(text(), 'According to ')]"
              "/descendant::a[contains(text(), 'Remodeling')]"
    )
    questions_form = Find(
        QuestionsFormBlock,
        by=By.XPATH,
        value="//div[@id='StepBodyId']"
    )

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
             waiting_for="zip input field is present",
             timeout_seconds=self.TIMEOUT)
        self.header.zip_input.send_keys(zip_text)

    @allure.step("Input siding area")
    @HomeBuddyBasePage.screen_after_step
    def input_siding_area(self, text: str):
        wait(lambda: self.questions_form.how_large_input_block.is_element_present("input_field"),
             waiting_for="Siding area input field is present",
             timeout_seconds=self.TIMEOUT)
        self.questions_form.how_large_input_block.input_field.send_keys(text)

    @allure.step("Input Full Name and Email")
    @HomeBuddyBasePage.screen_after_step
    def input_fullname_email(self, fullname: str, email: str):
        wait(lambda: self.questions_form.is_element_present("full_name_input"),
             waiting_for="Full name input field is present",
             timeout_seconds=self.TIMEOUT)
        wait(lambda: self.questions_form.is_element_present("email_input"),
             waiting_for="Email input field is present",
             timeout_seconds=self.TIMEOUT)
        self.questions_form.full_name_input.send_keys(fullname)
        self.questions_form.email_input.send_keys(email)

    @allure.step("Input Phone Number")
    @HomeBuddyBasePage.screen_after_step
    def input_phone_number(self):
        wait(lambda: self.questions_form.is_element_present("phone_input_field"),
             waiting_for="Phone number input field is present",
             timeout_seconds=self.TIMEOUT)
        self.questions_form.phone_input_field.send_keys(generate_phone_number())

    @allure.step("Choose type of project")
    @HomeBuddyBasePage.screen_after_step
    def choose_type_of_project(self):
        wait(lambda: len(self.questions_form.types_of_project_choices) == 5,
             waiting_for="5 types of project are present",
             timeout_seconds=self.TIMEOUT)
        self.questions_form.types_of_project_choices[4].click()

    @allure.step("Choose type of siding")
    @HomeBuddyBasePage.screen_after_step
    def choose_type_of_siding(self):
        wait(lambda: len(self.questions_form.types_of_siding_choices) == 5,
             waiting_for="5 types of siding are present",
             timeout_seconds=self.TIMEOUT)
        self.questions_form.types_of_siding_choices[4].click()

    @allure.step("Choose how many stories")
    @HomeBuddyBasePage.screen_after_step
    def choose_how_many_stories(self):
        wait(lambda: len(self.questions_form.how_many_stories_choices) == 4,
             waiting_for="4 stories choices is present",
             timeout_seconds=self.TIMEOUT)
        self.questions_form.how_many_stories_choices[0].click()

    @allure.step("Choose i am a homeowner")
    @HomeBuddyBasePage.screen_after_step
    def choose_homeowner_yes(self):
        wait(lambda: self.questions_form.is_element_present("homeowner_yes_choice"),
             waiting_for="'Are you the homeowner' Yes answer is present",
             timeout_seconds=self.TIMEOUT)
        self.questions_form.homeowner_yes_choice.click()

    @allure.step("Confirm phone number")
    @HomeBuddyBasePage.screen_after_step
    def confirm_phone(self):
        wait(lambda: self.questions_form.is_element_present("phone_confirmation_request"),
             waiting_for="Phone confirmation request is present",
             timeout_seconds=self.TIMEOUT)
        self.submit_click()

    @allure.step("Submit button click")
    @HomeBuddyBasePage.screen_after_step
    def submit_click(self):
        self.submit_button.click()
        self.wait_page_loading()

    @allure.step("Waiting for the page to load")
    @HomeBuddyBasePage.screen_after_step
    def wait_page_loading(self):
        wait(lambda: self.get_driver().execute_script("return document.readyState"),
             timeout_seconds=self.TIMEOUT,
             sleep_seconds=0.5,
             waiting_for="document.readyState returned True")
        wait(lambda: not self.is_element_present("submit_processing"),
             sleep_seconds=1, waiting_for="Submit progress animation is not present",
             timeout_seconds=self.TIMEOUT)

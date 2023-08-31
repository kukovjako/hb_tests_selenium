import allure

from selenium.webdriver.common.by import By
from waiting import wait
from webium import Find
from webium.controls.link import Link

from base.config import HB_SIDING_URL
from base.po.base import HomeBuddyBasePage
from base.po.elements import Header, SidingForYourHomeBlock, SidingTypesBlock, \
    AdvantagesOfNewSidingBlock, SidingPhotoGallery, IfNeedNewSidingBlock, HomeSeemBrandNewBlock, \
    MiddleZipBlock, HowItWorksBlock, TrustUsBlock, ReviewsBlock, BottomZipBlock, Footer


class HomeBuddySidingMainPage(HomeBuddyBasePage):
    header = Find(Header, by=By.CLASS_NAME, value="header")
    siding_for_your_home_block = Find(
        SidingForYourHomeBlock,
        by=By.XPATH,
        value="//h3[contains(text(), 'Siding For Your Home')]/ancestor::div/ancestor::section"
    )
    siding_types_block = Find(
        SidingTypesBlock,
        by=By.XPATH,
        value="//h3[contains(text(), 'Types Of Siding Projects')]/ancestor::div/ancestor::section"
    )
    advantages_of_new_siding_block = Find(
        AdvantagesOfNewSidingBlock,
        by=By.XPATH,
        value="//h3[contains(text(), 'Advantages Of New Siding')]/ancestor::div/ancestor::section"
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

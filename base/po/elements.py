from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds
from webium.controls.link import Link


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
    i_am_contractor_link = Find(
        Link,
        by=By.CLASS_NAME,
        value="header__navigation",
        context=WebElement
    )


class AdvantagesOfNewSidingBlock(WebElement):
    advantages_elements = Finds(   # 6 items
        by=By.XPATH,
        value="//ul[@class='advantages__list']/li"
    )


"""
These blocks have no use for this particular assignment. We could use it later.
Also PageObject just looks better this way.
"""


class SidingTypesBlock(WebElement):
    pass


class SidingForYourHomeBlock(WebElement):
    pass


class SidingPhotoGallery(WebElement):
    pass


class IfNeedNewSidingBlock(WebElement):
    pass


class HomeSeemBrandNewBlock(WebElement):
    pass


class MiddleZipBlock(WebElement):
    pass


class HowItWorksBlock(WebElement):
    pass


class TrustUsBlock(WebElement):
    pass


class ReviewsBlock(WebElement):
    pass


class BottomZipBlock(WebElement):
    pass


class Footer(WebElement):
    pass

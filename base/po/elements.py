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
        value="//ul[@class='advantages__list']/li",
        context=WebElement
    )


class HowLargeInputBlock(WebElement):
    input_field = Find(
        by=By.XPATH,
        value="//input[@type='tel']",
        context=WebElement
    )


class QuestionsFormBlock(WebElement):

    next_button = Find(
        by=By.XPATH,
        value="//button[@class='customButton']",
        context=WebElement
    )
    types_of_project_choices = Finds(  # 5 items
        by=By.CLASS_NAME,
        value="typeOfProject__item",
        context=WebElement
    )
    types_of_siding_choices = Finds(  # 5 items
        by=By.CLASS_NAME,
        value="kindOfSiding__item",
        context=WebElement
    )
    how_large_input_block = Find(
        HowLargeInputBlock,
        by=By.CLASS_NAME,
        value="howLargeCnt",
        context=WebElement
    )
    how_many_stories_choices = Finds(  # 4 items
        by=By.XPATH,
        # class name looks randomly generated or non-relatable in any way
        value="//input[@name='sdStories']/ancestor::div[position() = 1]",
        context=WebElement
    )
    homeowner_yes_choice = Find(
        by=By.XPATH,
        # class name looks randomly generated or non-relatable in any way
        value="//input[@name='internalOwner']/ancestor::div[position() = 1]",
        context=WebElement
    )
    # No reasonable class name on page for name+email block
    full_name_input = Find(
        by=By.XPATH,
        value="//input[@id='fullName']",
        context=WebElement
    )
    email_input = Find(
        by=By.XPATH,
        value="//input[@id='email']",
        context=WebElement
    )

    phone_input_field = Find(
        by=By.XPATH,
        value="//input[@id='phoneNumber']",
        context=WebElement
    )
    phone_confirmation_request = Find(
        by=By.XPATH,
        value="//h4[contains(text(), 'Please confirm your phone number.')]",
        context=WebElement
    )
    success_message = Find(
        by=By.XPATH,
        value="//h4[contains(text(), 'your contractor QA Customer will call soon')]",
        context=WebElement
    )


"""
These blocks have no use for this particular assignment. 
We could use them later for more detailed tests.
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

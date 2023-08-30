import pytest

from base.po.siding import HomeBuddySidingMainPage


@pytest.fixture
def setup():
    siding_page = HomeBuddySidingMainPage()
    if siding_page.get_driver().current_url != siding_page.url:
        siding_page.open()
        siding_page.wait_page_loading()
    return siding_page


@pytest.fixture(scope="module", autouse=True)
def divider_module(request):
    print('\n======== MODULE:[%s] ========' % request.module.__name__)

    def fin():
        print('\n======== FINISH MODULE:[%s] ========' % request.module.__name__)

    request.addfinalizer(fin)

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


@pytest.fixture(scope="session")
def page(request) -> Page:
    playwright = sync_playwright().start()
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "firefox":
        browser = get_firefox_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    elif browser_name == "chrome":
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    else:
        browser = get_chrome_browser(playwright)
        context = get_context(browser)
        page_data = context.new_page()
    yield page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium")


def get_firefox_browser(playwright) -> Browser:
    return playwright.firefox.launch(headless=True, slow_mo=50)


def get_chrome_browser(playwright) -> Browser:
    return playwright.chromium.launch(headless=True, slow_mo=100)


def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        locale="en-US",
        ignore_https_errors=True,
    )
    context.set_default_timeout(timeout=30000)
    return context


def pytest_collection_modifyitems(items):
    """Modifies test items in place to ensure test classes run in a given order."""
    CLASS_ORDER = ["TestSignInPage", "TestPortal", "TestNavBar", "TestsComments"]
    class_mapping = {item: item.cls.__name__ for item in items}

    sorted_items = items.copy()
    # Iteratively move tests of each class to the end of the test queue
    for class_ in CLASS_ORDER:
        sorted_items = [it for it in sorted_items if class_mapping[it] != class_] + [
            it for it in sorted_items if class_mapping[it] == class_
        ]
    items[:] = sorted_items


# def pytest_collection_modifyitems(items):
#     """Modifies test items in place to ensure test classes run in a given order."""
#     CLASS_ORDER = ["TestSignInPage", "TestsComments"]
#     class_mapping = {item: item.cls.__name__ for item in items}

#     sorted_items = items.copy()
#     # Iteratively move tests of each class to the end of the test queue
#     for class_ in CLASS_ORDER:
#         sorted_items = [it for it in sorted_items if class_mapping[it] != class_] + [
#             it for it in sorted_items if class_mapping[it] == class_
#         ]
#     items[:] = sorted_items

import pytest
from qaseio.pytest import qase
from pages.base_page import BasePage
from pages.result_page import ResultPage
from config import BASE_URL

class TestSearch:
    @qase.id(1)
    @qase.title(f"Visit to https://playwright.dev/python and search Auto-waiting.")
    @qase.description(
        f"Check that the controls on the authorization page appear and work."
    )
    def test_search(self, page):
        base_page = BasePage(page)
        base_page.visit(BASE_URL)
        base_page.navbar.open_search_modal()
        base_page.navbar.search_modal.search_history_is_empty()
        base_page.navbar.search_modal.search_text('Auto-waiting')
        result_page = ResultPage(page)
        result_page.result_page_title_text('Auto-waiting') is True
        result_page.navbar.open_search_modal()
        result_page.navbar.search_modal.search_history_not_empty()
        
        


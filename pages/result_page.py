from playwright.sync_api import Page

from pages.base_page import BasePage
from page_factory.title import Title


class ResultPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.result_page_title = Title(
            page, locator='header h1', name='Result page title'
        )

    def result_page_title_text(self, text):
        self.result_page_title.should_have_text(text=text) 
    
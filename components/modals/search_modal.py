from playwright.sync_api import Page

from page_factory.modal import Modal
from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title


class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.search_modal = Modal(
            page, locator='div[class="DocSearch-Modal"]', name="Search Modal"
        )
        self.search_input = Input(
            page, locator='input[class="DocSearch-Input"]', name="Search Input"
        )
        self.empty_dropdown_title = Title(
            page, locator='p[class="DocSearch-Help"]', name="Empty results"
        )
        self.search_history_list = ListItem(
            page, locator='li[class="DocSearch-Hit"]', name="Search History List"
        )

    def modal_is_opened(self):
        self.search_modal.should_be_visible()

    def search_history_is_empty(self):
        self.empty_dropdown_title.to_contain_text("No recent searches")

    def search_text(self, text):
        self.search_input.type_text(text=text)
        self.search_input.press('Space')
        self.search_input.press('Space')
        self.search_input.press('Enter')

    def search_history_not_empty(self):
        self.search_history_list.elements_should_be_visible()

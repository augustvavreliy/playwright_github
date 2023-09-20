from playwright.sync_api import Page

from page_factory.button import Button
from components.modals.search_modal import SearchModal


class Navbar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.search_modal = SearchModal(page)

        self.search_button = Button(
            page,
            locator='button[class="DocSearch DocSearch-Button"]',
            name="Navigation Search Button",
        )

    def open_search_modal(self): 
        self.search_button.should_be_visible()       
        self.search_button.click()
        self.search_modal.modal_is_opened()

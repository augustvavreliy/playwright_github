from abc import ABC, abstractmethod
from qaseio.pytest import qase
from playwright.sync_api import Locator, Page, expect


class Component(ABC):
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.name = name
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        return "component"

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def get_locators(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator).all()

    def click(self, **kwargs) -> None:
        with qase.step(f'Clicking {self.type_of} with name "{self.name}".'):
            locator = self.get_locator(**kwargs)
            locator.click()

    def should_be_visible(self, **kwargs) -> None:
        with qase.step(f'Checking that {self.type_of} "{self.name}" is visible.'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()

    def elements_should_be_visible(self, **kwargs) -> None:
        locator = self.get_locators(**kwargs)
        for element in locator:
            text = element.inner_text()
            with qase.step(
                f'Checking that {self.type_of} from "{self.name}" with "{text}" is visible.'
            ):
                expect(element).to_be_visible()

    def should_have_text(self, text: str, **kwargs) -> None:
        with qase.step(
            f'Checking that {self.type_of} "{self.name}" has text "{text}".'
        ):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(text)

    def to_contain_text(self, text: str, **kwargs) -> None:
        with qase.step(
            f'Checking that {self.type_of} "{self.name}" contain text "{text}".'
        ):
            locator = self.get_locator(**kwargs)
            array = []
            array.append(text)
            expect(locator).to_contain_text(array)

    def press(self, text, **kwargs) -> None:
        with qase.step(f'Press {text} on {self.type_of} with name "{self.name}".'):
            locator = self.get_locator(**kwargs)
            locator.page.keyboard.press(text)

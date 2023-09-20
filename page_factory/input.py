from qaseio.pytest import qase
from playwright.sync_api import expect

from page_factory.component import Component


class Input(Component):
    @property
    def type_of(self) -> str:
        return "input"
    
    def type_text(self, text: str, **kwargs) -> None:
        with qase.step(
            f'Type text on {self.type_of} "{self.name}" with text: "{text}".'
        ):
            locator = self.get_locator(**kwargs)
            locator.type(text)


    


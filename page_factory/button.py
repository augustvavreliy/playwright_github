from qaseio.pytest import qase

from page_factory.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return "button"

    def hover(self, **kwargs) -> None:
        with qase.step(f'Hovering over {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.hover()

    def double_click(self, **kwargs):
        with qase.step(f'Double clicking {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.dblclick()

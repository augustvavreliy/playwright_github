from page_factory.component import Component
from qaseio.pytest import qase


class Modal(Component):
    @property
    def type_of(self) -> str:
        return "modal"

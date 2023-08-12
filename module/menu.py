from abc import abstractmethod


class Menu:
    _name: str
    _description: str

    def __init__(self, name: str, desc: str):
        self.name = name
        self.description = desc

    @abstractmethod
    def execute(self, notes: list) -> list:
        pass

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.description

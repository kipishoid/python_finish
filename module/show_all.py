from abc import ABC

import tabulate

from module.menu import Menu


class ShowAll(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        result = [['id', 'name', 'description', 'date of changes']]
        for m in notes:
            result.append(notes[m].to_list())
        print(tabulate.tabulate(result))
        return notes

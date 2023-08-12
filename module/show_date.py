from abc import ABC

import tabulate

from module.menu import Menu


class ShowDate(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        key = tuple(input('enter the date separated by a space<YYYY MM DD> ->').strip().split())
        year, month, day = key
        result = [['id', 'name', 'description', 'date of changes']]
        for k in notes:
            if notes[k].get_date()[0:10] == year + '-' + month + '-' + day:
                result.append(notes[k].to_list())
        print(tabulate.tabulate(result))
        return notes

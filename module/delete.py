from abc import ABC

import tabulate

from module.menu import Menu


class Delete(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        key = int(input('enter the note number ->'))
        print(tabulate.tabulate([['id', 'name', 'description', 'date of changes'], notes[key].to_list()]))
        if input('delete Y/N?').lower() == 'y':
            notes.pop(key)
            print('deleted')
        else:
            print('cancel')
        return notes


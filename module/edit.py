from abc import ABC

import tabulate

from module.menu import Menu


class Edit(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        key = int(input('enter the note number ->'))
        print(tabulate.tabulate([['id', 'name', 'description', 'date of changes'], notes[key].to_list()]))
        if input('edit Y/N?').lower() == 'y':
            name, body = input('enter a new note name ->'), input('enter a new description ->')
            notes[key].__set__(name, body)
            print('edited')
        else:
            print('cancel')
        return notes

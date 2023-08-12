from control.control import Control
from module.add import Add
from module.delete import Delete
from module.edit import Edit
from module.exit import Exit
from module.read import Read
from module.save import Save
from module.show_all import ShowAll
from module.show_date import ShowDate
from module.show_id import ShowId


def start(control):
    print('_________Menu_________\n', ' help - \n')
    while True:
        try:
            key = input('->')
            control.on_execute(key)
        except KeyboardInterrupt:
            print("Exit")
            exit()


class View:
    control: Control

    def __init__(self):
        notes = {}
        self.control = Control(notes, [Read('read', 'read'),
                                       Edit('edit', 'edit'),
                                       Add('add', 'add'),
                                       Delete('del', 'delete'),
                                       Save('save', 'save to file'),
                                       ShowAll('shall', 'view the entire database'),
                                       ShowId('shid', 'view by number'),
                                       ShowDate('shdt', 'view by date'),
                                       Exit('exit', 'exit')])
        start(self.control)

    def get_control(self) -> Control:
        return self.control

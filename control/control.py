import tabulate


class Control:
    _menu: dict
    _notes: dict

    def __init__(self, notes: dict, menu: list):
        self.notes = notes
        temp = {}
        for m in menu:
            temp[m.get_name()] = m
        self.menu = temp

    def get_notes(self):
        return self.notes

    def get_menu(self):
        return self.menu

    def on_execute(self, key: str):
        if key == 'help':
            self.help()
        else:
            try:
                self.notes = self.menu[key].execute(self.notes)
            except KeyError:
                print("invalid value")

    def help(self):
        temp = []
        for k, v in self.get_menu().items():
            temp.append([k, v.get_desc()])
        print(tabulate.tabulate(temp))

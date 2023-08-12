import json
from abc import ABC

from data.note import Note
from module.menu import Menu


class Read(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        try:
            with open(f"{input('enter the file name ->')}.json", "r", encoding="UTF-8") as file:
                data = json.load(file)
                result = {}
                for j in data:
                    try:
                        note = Note(data[j]['id'], data[j]['name'], data[j]['body'], data[j]['date'])
                        result[note.get_id()] = note
                    except AttributeError:
                        print("incorrect structure")
                print("file uploaded")
                return result
        except FileNotFoundError:
            print("there is no file")

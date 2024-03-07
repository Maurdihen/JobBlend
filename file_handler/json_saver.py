import json
import os

from file_handler.base_file_handler import BaseFileHandler

class JSONSaver(BaseFileHandler):

    def __init__(self, file_path="./data/vacancies.json"):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False)

    def get_vacancies(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError:
            return []

    def save_vacancy(self, data):
        vacancies = self.get_vacancies()
        if data not in vacancies:
            vacancies.append(data)
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(vacancies, file, ensure_ascii=False)

    def delete_all_vacancy(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump("", file, ensure_ascii=False)

# data = {"title": "tete", "link": "ацуаыц", "рпропор": "ewrtw", "description": "rewtq"}
#
# temp = JSONSaver()
# temp.save_vacancy(data)

# temp.delete_vacancy(data)

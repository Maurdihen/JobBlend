import requests
from dotenv import load_dotenv
from api.base_api import BaseAPI

import os

from file_handler.json_saver import JSONSaver
from vacancies.vacancy import Vacancy

load_dotenv()

API_KEY = os.environ.get('API_KEY_SUPERJOB')

class SuperJobAPI(BaseAPI):

    def __init__(self):
        self._top_vacancies: list = None
        self._vacancies: list = None
        self._search_request: str = None
        self._params: dict = {}
        self._headers: dict = {
            'X-Api-App-Id': API_KEY
        }

    def _better_salary(self) -> None:
        for i in self._vacancies:
            if i['payment_from'] == 0 and i['payment_to'] != 0:
                i['payment_from'] = i['payment_to']
            if i['payment_from'] != 0 and i['payment_to'] == 0:
                i['payment_to'] = i['payment_from']

    def _better_vacancies(self) -> None:
        vacancies = []
        for i in self._vacancies:
            v = Vacancy(i['profession'], None, i['firm_name'], None, i['vacancyRichText'], i['payment_from'],
                        i['payment_to'], None, None, i['link'], None)
            vacancies.append(v.get_vacancy())
        self._vacancies = vacancies

    def get_vacancies(self, search_request: str) -> None:
        self._search_request = search_request
        self._params['keywords'] = search_request
        self._vacancies = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=self._headers,
                                       params=self._params).json()['objects']
        self._better_salary()
        self._better_vacancies()

    def get_top_vacancies(self, search_request: str, amount: int = 10) -> None:
        self.get_vacancies(search_request)
        temp = self._vacancies
        temp.sort(key=lambda x: x['salary_from'], reverse=True)
        self._top_vacancies = temp[:amount]

    def save_vacancies(self) -> None:
        """
        Save the retrieved vacancies to a JSON file.
        """
        saver = JSONSaver()
        print(self._vacancies)
        for i in self._vacancies:
            saver.save_vacancy(i)

    @property
    def vacancies(self) -> list:
        return self._vacancies

    @property
    def top_vacancies(self) -> list:
        return self._top_vacancies
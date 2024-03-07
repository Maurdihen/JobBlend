import requests
from dotenv import load_dotenv
from api.base_api import BaseAPI

import os

load_dotenv()

API_KEY = os.environ.get('API_KEY_SUPERJOB')

class SuperJobAPI(BaseAPI):

    def __init__(self):
        self._search_request = None
        self.params = {
            "keyword": self.search_request,
        }
        self.headers = {
            "X-Api-App-Id": API_KEY,
        }

    def connect_to_api(self):
        pass

    def get_vacancies(self):
        data = requests.get("https://api.superjob.ru/2.0/vacancies", params=self.params, headers=self.headers).json()
        return data


temp = SuperJobAPI("500000")
print(temp.get_vacancies())
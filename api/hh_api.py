from api.base_api import BaseAPI
from typing import Dict, Any, List
import requests

from file_handler.json_saver import JSONSaver
from vacancies.vacancy import Vacancy


class HeadHunterAPI(BaseAPI):

    def __init__(self) -> None:
        self.search_request: str = None
        self._vacancies: List[Vacancy] = []
        self._params: Dict[str, Any] = {
            'only_with_salary': 'true',
            'locale': "RU",
            'per_page': 100,
            "text": "",
            "salary": None,
            "currency": "RUR",
            "order_by": None
        }

    def get_vacancies(self, additional_params: Dict[str, Any]) -> List[Vacancy]:
        """
        Get a list of vacancies based on the provided additional parameters.

        Parameters:
        - additional_params (Dict[str, Any]): Additional parameters to customize the search.

        Returns:
        - List[Vacancy]: List of Vacancy objects representing the retrieved vacancies.
        """
        for k, v in additional_params.items():
            self._params[k] = v
        self._vacancies = requests.get("https://api.hh.ru/vacancies", params=self._params).json()["items"]
        vacancies: List[Vacancy] = []
        for i in self._vacancies:
            vacancy = Vacancy(
                name=i['name'],
                area_name=i['area']['name'],
                employer=i['employer']['name'],
                employment=i['employment']['name'],
                experience=i['experience']['name'],
                salary_from=i['salary']['from'],
                salary_to=i['salary']['to'],
                schedule=i['schedule']['name'],
                responsibility=i['snippet'].get('responsibility', ''),
                link=i['alternate_url'],
                currency=i['salary']["currency"]
            )
            vacancies.append(vacancy)
        self._vacancies = vacancies
        self._save_vacancies()
        return self._vacancies

    def _save_vacancies(self) -> None:
        """
        Save the retrieved vacancies to a JSON file.
        """
        saver = JSONSaver()
        for i in self._vacancies:
            saver.save_vacancy(i.get_vacancy())

    @property
    def vacancies(self) -> List[Vacancy]:
        """
        Get the list of retrieved vacancies.

        Returns:
        - List[Vacancy]: List of Vacancy objects.
        """
        return self._vacancies

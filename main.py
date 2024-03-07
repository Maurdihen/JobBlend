from pprint import pprint

from api.hh_api import HeadHunterAPI
from tools.hh_tools import get_current_currency


def user_interaction():
    hh_api = HeadHunterAPI()

    platform = input('Выберите платформу(superjob or hh.ru) введите ее название: \n')
    if platform == 'hh.ru':
        currency = input(f"Выберите одну валюты из предложенных или ничего не пишите\n{', '.join(list(get_current_currency().keys()))}\n")
        if currency == "":
            currency = "RUR"
        sort = input("Хотите ли вы отсортировать полученые валюты?\n"
                     "salary_desc - от большего к меньшему\n"
                     "salary_asc - от меньшего к большему\n"
                     "publication_time - по дате\n")
        if sort == "":
            sort = None
        text = input("Введите поисковой запрос:\n")
        salary = input("Введите зарплату на которую расчитываете\n")
        if salary == "":
            salary = None
        cnt = input("Введите сколько вакансий вы хотите получить от 1 до 100\n")
        if cnt == "":
            cnt = 10
        args = {"currency": currency, "order_by": sort, "salary": salary, "text": text, "per_page": cnt}
        vacancies = hh_api.get_vacancies(args)
        for i in vacancies:
            pprint(i.get_vacancy())



if __name__ == "__main__":
    user_interaction()

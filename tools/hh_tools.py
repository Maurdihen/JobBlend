import requests
import json

vacancy_search_order = [
    {"id": "publication_time", "name": "по дате"},
    {"id": "salary_desc", "name": "по убыванию дохода"},
    {"id": "salary_asc", "name": "по возрастанию дохода"},
    {"id": "relevance", "name": "по соответствию"},
    {"id": "distance", "name": "по удалённости"}
]

def get_current_currency():
    arr = {}
    req = requests.get("https://api.hh.ru/dictionaries").json()["currency"]
    for j in req:
        arr[j["code"]] = j["rate"]
    return arr



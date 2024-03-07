class Vacancy:

    def __init__(
        self, name, area_name, employer, employment, experience, salary_from, salary_to, schedule,
        responsibility, link, currency
    ):
        self._name = name
        self._area_name = area_name
        self._employer = employer
        self._employment = employment
        self._experience = experience
        self._salary_from = salary_from
        self._salary_to = salary_to
        self._schedule = schedule
        self._responsibility = responsibility
        self._link = link
        self._currency = currency

    def get_vacancy(self) -> dict:
        return {
            "name": self._name,
            "area_name": self._area_name,
            "employer": self._employer,
            "employment": self._employment,
            "experience": self._experience,
            "salary_from": self._salary_from,
            "salary_to": self._salary_to,
            "schedule": self._schedule,
            "responsibility": self._responsibility,
            "link": self._link,
            "currency": self._currency
        }

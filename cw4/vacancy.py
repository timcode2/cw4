import json


class Vacancy:
    def __init__(self, name, link, city, salary, requirement) -> None:
        self.name = name  # название вакансии
        self.link = link  # сылка на вакансию
        self.city = city  # местоположение
        self.salary = salary  # средняя заработная плата
        self.requirement = requirement  # требования к вакансии

    def __str__(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)

    def __lt__(self, other):
        return self.salary < other.salary
import json


class Vacancy:
    '''Создан класс для корректной структуры данных в JSON-файле'''
    def __init__(self, name, url, city, salary, description) -> None:
        self.name = name  # название вакансии
        self.url = url  # сылка на вакансию
        self.city = city  # местоположение
        self.salary = salary  # средняя заработная плата
        self.description = description  # требования к вакансии

    def __str__(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)

    def __lt__(self, other):
        if not isinstance(other, self.salary):
            raise ValueError('Невозможно сложить сумму')
        return self.salary < other.salary

    def __gt__(self, other):
        if not isinstance(other, self.salary):
            raise ValueError('Невозможно сложить сумму')
        return self.salary > other.salary

# проврерка на тип other  и магический метод __gt__

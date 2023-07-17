from abc import ABC, abstractmethod
import json


class VacancyStorage(ABC):
    '''СОздан абстрактный класс для работы с JSON-файлом'''
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_city(self, vacancies_list, city):
        pass


class JSONVacancyStorage(VacancyStorage):
    '''Класс для преобразования данных в JSON-формат и сохранения в отдельный файл'''
    def add_vacancy(self, vacancy_list):
        with open('vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(vacancy_list, f, indent=4, ensure_ascii=False)

    def get_vacancies_by_city(self, vacancies_list, city):
        city_vacancies = []
        for vacancy in vacancies_list:
            vacancy = json.loads(vacancy)
            if vacancy["city"] == city:
                city_vacancies.append(vacancy)
        return city_vacancies

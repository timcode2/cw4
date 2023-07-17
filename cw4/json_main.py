from abc import ABC, abstractmethod
import json


class VacancyStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass


class JSONVacancyStorage(VacancyStorage):
    def add_vacancy(self, vacancy_list):
        with open('vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(vacancy_list, f, indent=4, ensure_ascii=False)

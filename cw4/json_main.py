from abc import ABC, abstractmethod
import json


class VacancyStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONVacancyStorage(VacancyStorage):
    pass

import requests
import os
from abc import ABC, abstractmethod


class VacancyAPI(ABC):

    @abstractmethod
    def get_vacancy(self, keyword):
        pass


class HeadHunterAPI(VacancyAPI):
    pass


class SuperJobAPI(VacancyAPI):
    pass
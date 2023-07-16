import requests
import os
from abc import ABC, abstractmethod


class VacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(VacancyAPI):
    def get_vacancies(self, keyword):
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword, 'per_page': 100}
        response = requests.get(url, params=params)
        data = response.content.decode()
        response.close()
        return data


class SuperJobAPI(VacancyAPI):
    def get_vacancies(self, keyword):
        api_key: str = os.getenv('SUPERJOB_API_KEY')
        params = {'keyword': keyword, 'per_page': 100, 'count': 100}
        headers = {'X-Api-App-Id': api_key}
        url = 'https://api.superjob.ru/2.0/vacancies/'
        response = requests.get(url, params=params, headers=headers)
        data = response.content.decode()
        response.close()
        return data

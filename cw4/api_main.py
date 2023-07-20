import requests
import os
from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    '''Создан абстрактный класс для работы с API'''

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(VacancyAPI):
    '''Класс для работы с API hh.ru'''

    def get_vacancies(self, keyword):
        url = 'https://api.hh.ru/vacancies'
        data = []
        # Написать цикл для перехода по страницам
        for page in range(5):
            params = {'text': keyword, 'page': page, 'per_page': 100}
            response = requests.get(url, params=params).json()
            data.extend(response['items'])
        # Написать пустой список и добавлять через extend
        return data


class SuperJobAPI(VacancyAPI):
    '''Класс для работы с API superjob.ru'''

    def get_vacancies(self, keyword):
        api_key: str = os.getenv('SJ_API_KEY')
        data = []
        for page in range(5):
            params = {'keyword': keyword, 'page': page, 'per_page': 100}
            headers = {'X-Api-App-Id': api_key}
            url = 'https://api.superjob.ru/2.0/vacancies/'
            response = requests.get(url, params=params, headers=headers).json()
            data.extend(response['objects'])
        return data

import json
from vacancy import Vacancy


def add_hh_vacancies(hh_vacancies):
    hh_vacancies_dict = json.loads(hh_vacancies)["items"]
    hh_vacancies_list = []
    for vacancy in hh_vacancies_dict:
        name = vacancy["name"]
        url = 'https://hh.ru/vacancy/' + vacancy["id"]
        city = vacancy["area"]["name"]
        salary = 0
        if vacancy["salary"] is not None:
            salary_from = vacancy["salary"]["from"]
            salary_to = vacancy["salary"]["to"]
            if salary_from is not None and salary_to is not None:
                salary = int((salary_from + salary_to) // 2)
            elif salary_from is not None:
                salary = salary_from
            elif salary_to is not None:
                salary = salary_to
        else:
            salary = 0
        description = vacancy["snippet"]["requirement"]
        vacancy = Vacancy(name, url, city, salary, description)
        hh_vacancies_list.append(vacancy.__str__())
    return hh_vacancies_list


def add_sj_vacancies(sj_vacancies):
    sj_vacancies_dict = json.loads(sj_vacancies)["objects"]
    sj_vacancies_list = []

    for vacancy in sj_vacancies_dict:
        name = vacancy["profession"]
        url = 'https://api.superjob.ru/2.0/vacancies/' + str(vacancy["id"])
        city = vacancy["town"]["title"]

        if vacancy["payment_from"] > 0 and vacancy["payment_to"] > 0:
            salary = int((vacancy["payment_from"] + vacancy["payment_to"]) / 2)
        elif vacancy["payment_from"] > 0:
            salary = vacancy["payment_from"]
        elif vacancy["payment_to"] > 0:
            salary = vacancy["payment_to"]
        else:
            salary = 0

        description = vacancy["candidat"]
        vacancy = Vacancy(name, url, city, salary, description)
        sj_vacancies_list.append(vacancy.__str__())
    return sj_vacancies_list

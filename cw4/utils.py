from vacancy import Vacancy


# Созданы функции для работы с атрибутами данных словаря hh.ru и superjob.ru
def add_hh_vacancies(hh_vacancies):
    hh_vacancies_list = []
    for vacancy in hh_vacancies:
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
    sj_vacancies_list = []

    for vacancy in sj_vacancies:
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


def get_salary(vacancy):
    return vacancy.get('salary', 0)


def get_top_vacancies_by_salary(sorted_vacancies, user_top_count):
    top_vacancies = sorted(sorted_vacancies, key=get_salary, reverse=True)
    for vacancy in top_vacancies[:int(user_top_count)]:
        print(vacancy)

# Дописать функцию вывода топа и сортировки по зарплате sorted

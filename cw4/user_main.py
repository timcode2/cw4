from api_main import HeadHunterAPI, SuperJobAPI
from json_main import JSONVacancyStorage
from main import add_hh_vacancies, add_sj_vacancies


def user_menu():
    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()

    print('Введите название профессии для поиска вакансий')
    word = input()

    while True:
        print('''Выберите платформу для поиска вакансий
1 - hh.ru
2 - superjob.ru''')
        user_input = int(input())
        if user_input == 1:
            hh_vacancies = hh_api.get_vacancies(word)
            hh_vacancies_list = add_hh_vacancies(hh_vacancies)
            vacancies_list = hh_vacancies_list
            break
        elif user_input == 2:
            sj_vacancies = sj_api.get_vacancies(word)
            sj_vacancies_list = add_sj_vacancies(sj_vacancies)
            vacancies_list = sj_vacancies_list
            break
        else:
            print('Некорректный запрос')

    json_file = JSONVacancyStorage()
    print('Введите город для поиска вакансий')
    city = input()
    sorted_vacancies = json_file.get_vacancies_by_city(vacancies_list, city)
    json_file.add_vacancy(sorted_vacancies)


if __name__ == '__main__':
    user_menu()

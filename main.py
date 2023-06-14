from classes.db_manager import DBManager
from classes.hh_parser import HeadHunter
from config import config

PATH = 'vacancies.json'
PATH_2 = 'employers.json'


def main():
    params = config()
    db = DBManager('head_hunter', params)
    print('Создаем базу данных и таблицы')
    db2 = db.create_database()
    print(f'База данных и таблицы созданы')
    search_keyword = 'Python'
    hh = HeadHunter(search_keyword)
    k = hh.get_request()
    print('Добавляем данные из запроса в БД')
    db.insert_data_into_db(k)
    print("""Получаем список всех компаний и количество вакансий у каждой компании""")
    data = db.get_companies_and_vacancies_count()
    print(data)
    print("""Получаем список всех вакансий""")
    data_2 = db.get_all_vacancies()
    print(data_2)
    print("""Получает среднюю зарплату по вакансиям""")
    data_3 = db.get_avg_salary()
    print(data_3)
    print("""Получаем список всех компаний и количество вакансий у каждой компании""")
    data_4 = db.get_vacancies_with_higher_salary()
    print(data_4)
    print("""Получаем список всех компаний и количество вакансий у каждой компании""")
    data_5 = db.get_vacancies_with_keyword('python')
    print(data_5)


if __name__ == '__main__':
    main()

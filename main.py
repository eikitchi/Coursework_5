from classes.db_manager import *
from classes.hh_parser import *


def main():
    params = config()
    db = DBManager('head_hunter', params)
    hh = HeadHunter('Python')

    print('Вас приветстувует программа, которая создает базу данных по вакансиям.\n')
    db.create_database()
    print(f'База данных и таблицы созданы')
    print('Добавляем данные о работодателях и вакансиях')
    print('Ожидайте.')
    info = hh.get_vacancies_for_table
    for item in info:
        db.insert_in_employers(item['employer_id'], item['employer'], item['employer_url'])
        db.insert_in_vacancies(int(item['vacancy_id']), item['vacancy_name'], int(item['employer_id']),
                               item['description'], item['url'], item['payment_from'],
                               item['payment_to'], item['date_published'])
    print('Данные о работодателях и вакансиях добавлены')
    print('Вы можете вывести следующую информацию о вакансиях:\n'
          '1. Список всех компаний и количество вакансий у каждой компании.\n'
          '2. Список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n'
          '3. Среднюю зарплату по вакансиям.\n'
          '4. Список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n'
          '5. Список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”\n'
          'Введите цифру желаемой команды или же напишите "stop" для выхода из программы'
          )
    user_command = input('Команда: ')
    while user_command.lower() != 'stop':
        if user_command == '1':
            result = db.get_companies_and_vacancies_count()
            for i in result:
                print(i)
            user_command = input('Команда: ')
        elif user_command == '2':
            result = db.get_all_vacancies()
            for i in result:
                print(i)
            user_command = input('Команда: ')
        elif user_command == '3':
            result = db.get_avg_salary()
            for i in result:
                print(i)
            user_command = input('Команда: ')
        elif user_command == '4':
            result = db.get_vacancies_with_higher_salary()
            for i in result:
                print(i)
            user_command = input('Команда: ')
        elif user_command == '5':
            keyword = str(input('Введите ключевое слово '))
            result = db.get_vacancies_with_keyword(keyword)
            for i in result:
                print(i)
            user_command = input('Команда: ')


if __name__ == '__main__':
    main()

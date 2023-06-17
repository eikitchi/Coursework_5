import json
import time

import requests


class HeadHunter:
    """
    Класс платформы
    HH
    """
    URL = 'https://api.hh.ru/vacancies/'

    def __init__(self, search_keyword):
        """
        Инициализирует слово,
        по которому происходит поиск вакансий
        """
        super().__init__()
        self.search_keyword = search_keyword
        self.params = {
            'text': f'{self.search_keyword}',
            'per_page': 100,
            'area': 113,
            'page': 0
        }

    def get_request(self):
        """
        Получает вакансии по API
        """
        response = requests.get(self.URL, params=self.params)
        data = response.content.decode()
        response.close()
        json_hh = json.loads(data)
        return json_hh

    @property
    def get_request_employer_id(self):
        """
        Получает список работодателей
        """
        employers_list = []
        for i in range(15):
            data = self.get_request()
            request_hh = data.get('items')
            for item in request_hh:
                if len(employers_list) == 15:
                    break
                else:
                    employers_list.append(item.get('employer').get('id'))

        return employers_list

    def info_vacancies_for_table(self, vacancies):
        """
        Структурирует получаемые
        из API данные по
        ключам для таблиц
        """
        data = {
            'vacancy_id': vacancies.get('id'),
            'vacancy_name': vacancies.get('name'),
            'employer_id': int(vacancies.get('employer').get('id')),
            'employer': vacancies.get('employer').get('name'),
            'employer_url': vacancies.get('employer').get('url'),
            'description': vacancies.get('snippet').get('responsibility'),
            'url': vacancies.get('alternate_url'),
            'payment_from': vacancies['salary']['from'],
            'payment_to': vacancies['salary']['to'],
            'date_published': vacancies.get('published_at'),
        }

        return data

    @property
    def get_vacancies_for_table(self):
        """
        Получает вакансии
        при наличии информации
        о ЗП и по нужному работодателю
        """
        employers_hh = []
        list_employers = self.get_request_employer_id
        data = self.get_request()
        items = data.get('items')
        while True:
            if not items:
                break
            for employer_hh in items:
                if employer_hh.get('salary') is not None and employer_hh.get('salary').get('currency') == 'RUR':
                    if employer_hh.get('employer').get('id') in list_employers:
                        employers_hh.append(self.info_vacancies_for_table(employer_hh))
                    else:
                        continue

            self.params['page'] += 1
            time.sleep(0.2)
            if data.get('pages') == self.params['page']:
                break

        return employers_hh

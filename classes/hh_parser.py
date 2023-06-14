import json
import time

import requests


class HeadHunter:
    URL = f'https://api.hh.ru/vacancies'

    def __init__(self, search_keyword):
        self.params = {'text': f'{search_keyword}',
                       'page': 0,
                       'per_page': 100}

    def get_request(self):
        """Запрос к API HH"""
        response = requests.get(self.URL, self.params)
        if response.status_code == 200:
            data = response.json()
            return data


def get_request_company(self):
    """
    Парсим компании с ресурса HeadHunter
    """
    url = 'https://api.hh.ru/vacancies?text=' + search_keyword
    company_id = []
    for item in range(15):
        request_hh = requests.get(url, params={"keywords": search_keyword}).json()['items']
        time.sleep(0.5)
        for item2 in request_hh:
            if len(company_id) == 15:
                break
            company_id.add(item2['employer']['id'])
    return company_id


def get_employers(self):
    """Получает список компаний и их id"""
    employers = []
    data = self.get_request()
    items = data.get('items')
    for item in items[:15]:
        if item.get('employer').get('id') != 0 and item.get('employer').get('name') != 0:
            employers.append((item.get('employer').get('id'),
                              item.get('employer').get('name')))
        unigue_employers = list(set(employers))
    with open('employers.json', 'w', encoding="UTF-8") as file:
        json.dump(unigue_employers, file, indent=4, ensure_ascii=False)
    return unigue_employers


@staticmethod
def get_info(data):
    """Структурирует получаемые из API данн"""

    vacancy_id = int(data.get('id'))
    name = data['name']
    employer_id = int(data.get('employer').get('id'))
    city = data.get('area').get('name')
    url = data.get('alternate_url')

    if 'salary' in data.keys():
        if data.get('salary') is not None:
            if 'from' in data.get('salary'):
                salary = data.get('salary').get('from')
            else:
                salary = None
        else:
            salary = None
    else:
        salary = None

    vacancy = (vacancy_id, name, employer_id, city, salary, url)
    return vacancy


def get_vacancies(self):
    vacancies = []
    page = 0
    while True:
        self.params['page'] = page
        data = self.get_request()
        for vacancy in data.get('items'):
            if vacancy.get('salary') is not None and vacancy.get('salary').get('currency') is not None:
                if vacancy.get('salary').get('currency') == "RUR":
                    vacancies.append(self.get_info(vacancy))
                else:
                    continue
            else:
                vacancies.append(self.get_info(vacancy))

        page += 1
        time.sleep(0.2)

        if data.get('pages') == page:
            break
    with open('vacancies.json', 'w', encoding="UTF-8") as file:
        json.dump(vacancies, file, indent=4, ensure_ascii=False)
    vacancy_lst = list(vacancies)
    return vacancies


if __name__ == '__main__':
    search_keyword = 'Python'
    hh = HeadHunter(search_keyword)
    # o = hh.get_request_company()
    # print(o)
    k = hh.get_request()
    print(k)
    # print(type(k))
    # m = hh.get_vacancies()
    # print(m)
    # print(type(m))
    # with open('data1.json', 'r', encoding="utf8") as f:
    # data = json.load(f)

    # l = hh.get_employers()
    # print(l)

import requests
import fake_useragent
from bs4 import BeautifulSoup

from person import Person

def parse(id: int) -> list:
    URL = 'https://official.contest.yandex.ru/contest/' + str(id) + '/standings/'

    res = []
    for p in range(1, 1000):
        params = {'p': p}

        user_agent = fake_useragent.UserAgent().random
        header = {'user-agent': user_agent}

        response = requests.get(URL, params=params, headers=header)
        soup = BeautifulSoup(response.text, "lxml")

        table = soup.find('tbody', class_='table__body')

        if not table:
            break

        rows = table.find_all('tr', class_='table__row')
        for row in rows:
            person = Person()

            person.place = row.find('td', class_='table__cell_role_place').text
            person.name = row.find('div', class_='table__data_type_ptp').text

            tasks = row.find_all('td', class_='table__cell_role_result')
            for task in tasks:
                person.tasks_count += 1
                points = task.find('span', class_='standings-cell__score').text
                person.points.append(int(points) if points != '—' else points)
            person.total_points = int(row.find('td', class_='table__cell_role_meta').text)

            res.append(person)

    return res

if __name__ == '__main__':
    id = int(input())
    p = parse(id)
    for person in p:
        print(person)

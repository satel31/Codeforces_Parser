import requests

from parser.models import Problem


def request_data() -> dict:
    """Gets data about problems from codeforces.com"""
    url: str = "https://codeforces.com/api/problemset.problems"
    response = requests.get(url)

    if response.status_code == 200:
        vacancies = response.json()
        return vacancies['result']
    else:
        print("Error:", response.status_code)


def problem_data_create() -> None:
    """Compiling dictionaries with the necessary data to be entered into the database in the problem table"""
    problem_data = request_data()
    problem_db = []
    for p in problem_data['problems']:
        print(p)
        if Problem.objects.filter(problem_name=p['name']).count() == 0:
            problem = {'topics': ', '.join(p['tags']),
                       'solutions_amount': int([pr['solvedCount'] for pr in problem_data['problemStatistics'] if
                                                pr['contestId'] == p['contestId'] and pr['index'] == p['index']][0]),
                       'problem_name': p['name'],
                       'index': p['index'],
                       'rating':  p['rating']
                       }
            problem_db.append(Problem(**problem))
    Problem.objects.bulk_create(problem_db)
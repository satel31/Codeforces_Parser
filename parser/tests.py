from rest_framework import status
from rest_framework.test import APITestCase

from parser.models import Problem


class ProblemTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = '/parser/'
        self.data = {
            'topics': 'test',
            'solutions_amount': 20,
            'problem_name': 'test',
            'index': 'test',
        }
        self.problem = Problem.objects.create(**self.data)

    def test_1_create_problem(self):
        """Problem creation testing """

        response = self.client.post(f'{self.url}add_problems/')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(Problem.objects.all().count(), 0)

    def test_2_list_problem(self):
        """Problem list testing """
        response = self.client.get(f'{self.url}problems/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'problem_name': 'test', 'rating': None, }]
        )

    def test_4_retrieve_problem(self):
        """Problem retrieve testing """

        response = self.client.get(f'{self.url}problems/{self.problem.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'problem_name': 'test', 'rating': None, 'topics': 'test', 'solutions_amount': 20, 'index': 'test'}
        )

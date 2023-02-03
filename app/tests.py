import unittest
import requests
from environs import Env

env = Env()
env.read_env()

url = f"{env.str('HOST')}:{env.int('PORT')}/"


class TestGetTeasers(unittest.TestCase):
    def test_get_teasers_author(self):
        author_user = requests.post(url + 'auth/token/login/',
                                    json={'username': 'AuthorUser', 'password': 'userpassword1'}).json()
        headers = {'Authorization': 'Token ' + author_user.get('auth_token')}
        self.assertIsInstance(requests.get(url + 'api/teaser/', headers=headers).json(), list)

    def test_get_teasers_simple_user(self):
        simple_user = requests.post(url + 'auth/token/login/',
                                    json={'username': 'SimpleUser', 'password': 'userpassword1'}).json()
        headers = {'Authorization': 'Token ' + simple_user.get('auth_token')}
        self.assertDictEqual(requests.get(url + 'api/teaser/', headers=headers).json(),
                             {'detail': 'You do not have permission to perform this action.'})

    def test_get_teasers_admin_user(self):
        admin_user = requests.post(url + 'auth/token/login/', json={'username': 'qwe', 'password': 'qwe'}).json()
        headers = {'Authorization': 'Token ' + admin_user.get('auth_token')}
        self.assertIsInstance(requests.get(url + 'api/teaser/', headers=headers).json(), list)


class TestAddTeasers(unittest.TestCase):
    def test_add_teaser_author(self):
        author_user = requests.post(url + 'auth/token/login/',
                                    json={'username': 'AuthorUser', 'password': 'userpassword1'}).json()
        headers = {'Authorization': 'Token ' + author_user.get('auth_token')}
        body = {
            "title": "1",
            "description": "1",
            "category": "1",
        }
        self.assertEqual(requests.post(url + 'api/teaser/', headers=headers, json=body).json(), 0)

    def test_add_teaser_admin(self):
        admin = requests.post(url + 'auth/token/login/',
                              json={'username': 'qwe', 'password': 'qwe'}).json()
        headers = {'Authorization': 'Token ' + admin.get('auth_token')}
        body = {
            "title": "1",
            "description": "1",
            "category": "1",
        }
        self.assertEqual(requests.post(url + 'api/teaser/', headers=headers, json=body).json(), -1)

    def test_add_teaser_simple_user(self):
        simple_user = requests.post(url + 'auth/token/login/',
                                    json={'username': 'SimpleUser', 'password': 'userpassword1'}).json()
        headers = {'Authorization': 'Token ' + simple_user.get('auth_token')}
        body = {
            "title": "1",
            "description": "1",
            "category": "1",
        }
        self.assertDictEqual(requests.post(url + 'api/teaser/', headers=headers, json=body).json(),
                             {'detail': 'You do not have permission to perform this action.'})


class TestChangeTeasers(unittest.TestCase):
    def test_change_teaser_admin(self):
        admin = requests.post(url + 'auth/token/login/',
                              json={'username': 'qwe', 'password': 'qwe'}).json()
        headers = {'Authorization': 'Token ' + admin.get('auth_token')}
        body = {
            "id": "26",
            "status": 'paid'
        }
        self.assertIsInstance(requests.post(url + 'api/change_teaser_state/', headers=headers, json=body).json(), dict)

    def test_change_teasers_admin(self):
        admin = requests.post(url + 'auth/token/login/',
                              json={'username': 'qwe', 'password': 'qwe'}).json()
        headers = {'Authorization': 'Token ' + admin.get('auth_token')}
        body = [
            {
                "id": "26",
                "status": 'paid'
            },
            {
                "id": "27",
                "status": 'paid'
            },
            {
                "id": "28",
                "status": 'failure'
            }
        ]
        self.assertIsInstance(requests.post(url + 'api/change_teaser_state/', headers=headers, json=body).json(), dict)

    def test_change_teaser_author(self):
        author = requests.post(url + 'auth/token/login/',
                               json={'username': 'AuthorUser', 'password': 'userpassword1'}).json()
        headers = {'Authorization': 'Token ' + author.get('auth_token')}
        body = {
            "id": "26",
            "status": 'paid'
        }
        self.assertDictEqual(requests.post(url + 'api/change_teaser_state/', headers=headers, json=body).json(),
                             {'detail': 'You do not have permission to perform this action.'})

    def test_change_teaser_simple_user(self):
        simple_user = requests.post(url + 'auth/token/login/',
                                    json={'username': 'SimpleUser', 'password': 'userpassword1'}).json()
        headers = {'Authorization': 'Token ' + simple_user.get('auth_token')}
        body = {
            "id": "26",
            "status": 'paid'
        }
        self.assertDictEqual(requests.post(url + 'api/change_teaser_state/', headers=headers, json=body).json(),
                             {'detail': 'You do not have permission to perform this action.'})

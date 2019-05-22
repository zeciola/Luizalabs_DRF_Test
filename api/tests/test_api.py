from tests.base_test_api import AppEmployeeAPITestCase

class TestEmployee(AppEmployeeAPITestCase):
    
    def test_employee_get_method(self):

        print('In test get employee')

        endpoint = 'employee/'

        token = self.token

        auth = {'Authorization': f'Token {token.key}'}

        response = self.client.get(self.base_url+endpoint, headers=auth)

        except_response = {'name': 'Testando', 'email': 'test@test.test', 'department': 'Testing depart'}

        self.assertEqual(response.json()[0], except_response)

    def test_employee_get_two(self):

        ...


    ...
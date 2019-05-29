from tests.base_test_api import AppEmployeeAPITestCase
from app_employee.models import Employee

class TestEmployee(AppEmployeeAPITestCase):
    
    def test_employee_get_method(self):

        print('In test get employee')

        endpoint = 'employee/'

        token = self.token

        auth = {'Authorization': f'Token {token.key}'}

        response = self.client.get(self.base_url+endpoint, headers=auth, format='json')

        except_response = [{'name': 'Testando', 'email': 'test@test.test', 'department': 'Testing depart'}]

        self.assertEqual(response.json(), except_response)

    def test_employee_get_first(self):

        print('In test get first employee')

        endpoint = 'employee/'

        token = self.token

        auth = {'Authorization': f'Token {token.key}'}

        response = self.client.get(self.base_url+endpoint+'1/', headers=auth, format='json')

        except_response = {'name': 'Testando', 'email': 'test@test.test', 'department': 'Testing depart'}

        self.assertEqual(response.json(), except_response)

        ...

    def test_employee_get_two(self):

        Employee.objects.create(
            name='Testando1', 
            email ='test1@test1.test1', 
            department='Testing 1 depart '
            )
        

        endpoint = 'employee/'

        token = self.token

        auth = {'Authorization': f'Token {token.key}'}

        response = self.client.get(self.base_url+endpoint, headers=auth)

        self.assertEqual(len(response.json()), 2)

        ...


    def test_employee_post(self):

        endpoint = 'employee/'

        token = self.token

        auth = {'Authorization': f'Token {token.key}'}

        data = {'name':'Post_test','email':'post@post@post.com','department':'post depart'}

        response = self.client.post(self.base_url+endpoint, data=data,headers=auth)

        print(response.json())

        self.assertEqual(len(response.json()), 2)
        
        ...

    ...
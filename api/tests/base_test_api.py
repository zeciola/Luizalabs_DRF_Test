from rest_framework.test import APITestCase
from requests.auth import HTTPBasicAuth
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


from app_employee.models import Employee


class AppEmployeeAPITestCase(APITestCase):
    
    def setUp(self):

        print('Seting Up . . .')

        self.base_url = 'http://127.0.0.1:8000/'

        #Admin create
        self.adminuser = User.objects.create_user('admin', 'admin@test.com', 'pass')
        self.adminuser.save()
        self.adminuser.is_staff = True
        self.adminuser.save()

        # Admin Auth
        self.token = Token.objects.get(user__username='admin')

        print(f'token key setUp: {self.token.key}')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.client.login(username='admin', password='pass')

        self.client.session.auth = HTTPBasicAuth('admin', 'pass')

        Employee.objects.create(
            name='Testando', 
            email ='test@test.test', 
            department='Testing depart'
            )
        
    def create_employee(name,email,department):
        Employee.objects.create(
            name=name, 
            email =email, 
            department=department
            )
    
    def tearDown(self):
        print('Tear Down . . .')

        self.client.logout()

        print('Logout')

        ...
    
    ...


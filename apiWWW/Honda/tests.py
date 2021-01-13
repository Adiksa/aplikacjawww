from django.utils.http import urlencode
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from . import views
from .models import Silnik

# Create your tests here.

class SilniksTests(APITestCase):
    def post_silnik(self, _kod, _pojemnosc, _moc, _odciecieObrotow, _kompresja, _is_login, _username, _email, _password):
        user = User.objects.create_user(_username, _email, _password)
        if _is_login:
            self.client.login(username=_username, password=_password)
        url = reverse(views.SilnikList.name)
        data = {
            'kod' : _kod,
            'pojemnosc' : _pojemnosc,
            'moc' : _moc,
            'odciecieObrotow' : _odciecieObrotow,
            'kompresja' : _kompresja
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_silnik_without_login(self):
        response = self.post_silnik('D14A3',1396,75,7200,'9.1:1',False,'test','mail@testowy.pl','sprawdzam')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_silnik_with_login(self):
        response = self.post_silnik('D14A3',1396,75,7200,'9.1:1',True,'test','mail@testowy.pl','sprawdzam')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_silnik_user(self):
        self.post_silnik('D14A3',1396,75,7200,'9.1:1',True,'test','mail@testowy.pl','sprawdzam')
        user = User.objects.all()[0]
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'mail@testowy.pl')
        self.assertTrue(user.check_password('sprawdzam'))

    def test_count_objects(self):
        self.post_silnik('D14A3',1396,75,7200,'9.1:1',True,'test','mail@testowy.pl','sprawdzam')
        self.post_silnik('D14A3',1396,75,7200,'9.1:1',True,'test2','mail@testowy.pl','sprawdzam')
        self.post_silnik('D14A3',1396,75,7200,'9.1:1',True,'test3','mail@testowy.pl','sprawdzam')
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 3)

    def test_student_return_string(self):
        self.post_silnik('D14A3',1396,75,7200,'9.1:1',True,'test','mail@testowy.pl','sprawdzam')
        silnik = Silnik.objects.all()[0]
        self.assertEqual(str(silnik), 'D14A3')
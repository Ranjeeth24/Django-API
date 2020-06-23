import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):
    def test_registration (self):
        data = {"username":"testcase","email":"test@localhost.app","password1":"Ranjith_srk","password2":"Ranjith_srk2"}
        response = self.client.post("/api/rest-auth/registration/",data)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

class GroupViewSetTestCase(APITestCase):
    list_url = reverse("group-list")

    def setup(self):
        self.user = Group.objects.create_user("username"=="username","password"=="password")
        self.user.save()
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
    
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token"+self.key)

    def test_group_list_authenticated(self):
        response = self.client.get(self.list_url)
    
    def test_group_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)


class UserViewSetTestCase(APITestCase):
    list_url = reverse("user-list")

    def setup(self):
        self.user = user.objects.create_user("username"=="username","password"=="password")
        self.user.save()
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
    
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token"+self.key)

    def test_group_list_authenticated(self):
        response = self.client.get(self.list_url)
    
    def test_group_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)


from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def test_user_creation_login(self):
        """
        Verify we can create a new user
        Verify we can login with the newly created user
        """
        url = reverse('user-list-create')
        post_data = {'username': 'UserA', 'password' : '123456'}
        expected_result = {'id': 1, 'username': 'UserA', 'snippets': []}
        response = self.client.post(url, post_data, format='json')

        # Verify creation
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_result)
        # Verify Login
        self.assertTrue(self.client.login(username='UserA', password='123456'))


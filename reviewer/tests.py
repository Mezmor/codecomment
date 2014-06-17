from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from reviewer.models import User, Snippet, Comment


class FlowTests(APITestCase):
    def test_list_create_users(self):
        """
        Verify a user can be created. (Create two)
        Verify we can login as a user.
        Verify we can see all users when logged in & logged out
        """
        url = reverse('user-list-create')
        user_data = [{'username': 'UserA', 'password': '123456'},
                          {'username': 'UserB', 'password': '123456'}]

        expected_users = [{'id': 1, 'username': 'UserA', 'snippets': []},
                          {'id': 2, 'username': 'UserB', 'snippets': []}]
        # Verify creation
        response = self.client.post(url, user_data[0], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_users[0])

        # Create second user
        response = self.client.post(url, user_data[1], format='json')

        # Verify user list
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_users)

        # Verify Login
        self.assertTrue(self.client.login(username='UserA', password='123456'))

        # Verify user list
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_users)

    def test_create_snippet(self):
        """
        Verify we can not create a Snippet if not logged in
        Verify we can create a Snippet if logged in (create two)
        Verify we can see all Snippets when logged in & logged out
        """
        test_user = User.objects.create(username='UserA', password='123456')

        url = reverse('snippet-list-create')
        snippet_data = [{'title':'Test code',
                        'code': 'a=["hello", "world"]\nfor word in a:\n\tprint word',
                        'display_linenos': True,
                        'owner': test_user},
                        {'title':'Test code',
                         'code': 'a=["hello", "world"]\nfor word in a:\n\tprint word',
                         'display_linenos': True,
                         'owner': test_user}]

        # Verify creating a snippet is not allowed without logging in
        response = self.client.post(url, snippet_data[0], format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


        self.assertEqual(response.status_code, )
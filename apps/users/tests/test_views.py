from django.test import TestCase
from django.test import Client
from unittest import mock

from rest_framework.utils import json


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    # Happy path
    def test_get_existent_user(self):
        response = self.client.get('/settings/user/2')
        expected = '{"id":2,"integration_id":"f65f7934-29ca-4fdd-9fcc-79d45439c478","name":"Marge Simpson",' \
                   '"email":"marge@email.com"}'
        content = response.content.decode('utf-8')
        self.assertEquals(content, expected)
        self.assertEqual(response.status_code, 200)

    def test_put_existent_user(self):
        response = self.client.put('/settings/user/1', data={'name': 'Bart Simpson', 'email': 'bart@email.com'},
                              content_type='application/json')
        expected = '{"id":1,"integration_id":"2a81fc13-c919-4dbc-8f71-8b2d0f0b5e77","name":"Bart Simpson",' \
                   '"email":"bart@email.com"}'
        content = response.content.decode('utf-8')
        self.assertEquals(content, expected)
        self.assertEqual(response.status_code, 200)

    # User not found
    def test_get_non_existent_user(self):
        response = self.client.get('/settings/user/99')
        expected = '{"error":"User not found"}'
        # Decode bytes to string
        content = response.content.decode('utf-8')
        self.assertEquals(content, expected)
        self.assertEqual(response.status_code, 404)

    def test_put_non_existent_user(self):
        response = self.client.put('/settings/user/99')
        expected = '{"error":"User not found"}'
        # Decode bytes to string
        content = response.content.decode('utf-8')
        self.assertEquals(content, expected)
        self.assertEqual(response.status_code, 404)

    # Update readonly fields should be ignored and stay the same
    def test_put_update_read_only_fields(self):
        response = self.client.put('/settings/user/1', data={'id': '99', 'name': 'Bart Simpson', 'email': 'bart@email.com',
                                                        'integration_id': 'abc'},
                              content_type='application/json')
        expected = '{"id":1,"integration_id":"2a81fc13-c919-4dbc-8f71-8b2d0f0b5e77","name":"Bart Simpson",' \
                   '"email":"bart@email.com"}'
        content = response.content.decode('utf-8')
        self.assertEquals(content, expected)
        self.assertEqual(response.status_code, 200)

    # Validations
    def test_put_update_without_name(self):
        response = self.client.put('/settings/user/1', data={'email': 'bart@email.com'}, content_type='application/json')
        expected = '{"error":{"name":["This field is required."]}}'
        content = response.content.decode('utf-8')
        self.assertEquals(content, expected)
        self.assertEqual(response.status_code, 400)

    def test_put_update_without_email(self):
        response = self.client.put('/settings/user/1', data={'name': 'Bart Simpson'}, content_type='application/json')
        expected = '{"error":{"email":["This field is required."]}}'
        content = response.content.decode('utf-8')
        self.assertEquals(content, expected)
        self.assertEqual(response.status_code, 400)

from apps.integrations import integrations
from django.test import TestCase
from unittest.mock import patch
from apps.integrations.mock_lib.mock import Status
from apps.users.models import User


class IntegrationsTestCase(TestCase):
    def setUp(self):
        self.user = User(id=1, name='test', email='valid@email.com', integration_id='abc')

    # Mocking Mocklib to return SUCCESS
    @patch('apps.integrations.mock_lib.mock.MockLib.update_user', return_value=Status.SUCCESS)
    def test_update_user_external_system_success(self, mock_update_user):
        with self.assertLogs("apps.integrations.integrations") as logger:
            integrations.update_user_external_system(self.user)
            self.assertListEqual(logger.output,
                                 ["INFO:apps.integrations.integrations:User 1 updated on external system"])

    # Mocking Mocklib to return FAIL
    @patch('apps.integrations.mock_lib.mock.MockLib.update_user', return_value=Status.FAIL)
    def test_update_user_external_system_fail(self, mock_update_user):
        with self.assertLogs("apps.integrations.integrations") as logger:
            integrations.update_user_external_system(self.user)
            self.assertListEqual(logger.output,
                                 ["ERROR:apps.integrations.integrations:External system failed to update user 1"])

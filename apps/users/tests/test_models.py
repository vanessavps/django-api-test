from django.test import TestCase
from apps.users.models import User
from django.core.exceptions import ValidationError


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User(name='test', email='valid@email.com', integration_id='abc')

    # Happy path
    def test_user_save(self):
        self.user.save()
        self.assertTrue(User.objects.filter(id=self.user.id).exists())

    # Invalid field content
    def test_invalid_email_validation(self):
        self.user.email = 'invalid@email'
        with self.assertRaisesMessage(ValidationError, "{'email': ['Enter a valid email address.']}"):
            self.user.full_clean()

    def test_name_exceeded_max_length(self):
        self.user.name = 'testfieldwithmorethan70charactersIthinkthisisalreadytoomuchbutitseemsok'
        with self.assertRaisesMessage(ValidationError,
                                      "{'name': ['Ensure this value has at most 70 characters (it has 71).']}"):
            self.user.full_clean()

    def test_email_exceeded_max_length(self):
        self.user.email = 'testfieldwithmorethan70characters@Ithinkthisisalreadytoomuchbutitseems.ok'
        with self.assertRaisesMessage(ValidationError,
                                      "{'email': ['Ensure this value has at most 70 characters (it has 73).']}"):
            self.user.full_clean()

    def test_integration_id_exceeded_max_length(self):
        self.user.integration_id = 'testfieldwithmorethan70charactersIthinkthisisalreadytoomuchbutitseemsok'
        with self.assertRaisesMessage(ValidationError,
                                      "{'integration_id': ['Ensure this value has at most 70 characters (it has 71).']}"):
            self.user.full_clean()

    # Empty fields
    def test_email_should_not_be_empty(self):
        self.user.email = ''
        with self.assertRaisesMessage(ValidationError, "{'email': ['This field cannot be blank.']}"):
            self.user.full_clean()

    def test_name_should_not_be_empty(self):
        self.user.name = ''
        with self.assertRaisesMessage(ValidationError, "{'name': ['This field cannot be blank.']}"):
            self.user.full_clean()

    def test_integration_id_should_not_be_empty(self):
        self.user.integration_id = ''
        with self.assertRaisesMessage(ValidationError, "{'integration_id': ['This field cannot be blank.']}"):
            self.user.full_clean()

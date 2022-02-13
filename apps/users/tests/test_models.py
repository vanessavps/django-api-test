from django.test import TestCase
from apps.users.models import User
from django.core.exceptions import ValidationError


class ModelsTestCase(TestCase):
    # Happy path
    def test_user_save(self):
        user = User(name='test', email='valid@email.com', integration_id='abc')
        user.save()
        self.assertTrue(User.objects.filter(id=user.id).exists())

    # Invalid field content
    def test_invalid_email_validation(self):
        user = User(name='test', email='invalid@email', integration_id='abc')
        with self.assertRaisesMessage(ValidationError, "{'email': ['Enter a valid email address.']}"):
            user.full_clean()

    def test_name_exceeded_max_length(self):
        user = User(name='testfieldwithmorethan70charactersIthinkthisisalreadytoomuchbutitseemsok',
                    email='valid@email.com', integration_id='abc')
        with self.assertRaisesMessage(ValidationError,
                                      "{'name': ['Ensure this value has at most 70 characters (it has 71).']}"):
            user.full_clean()

    def test_email_exceeded_max_length(self):
        user = User(name='test',
                    email='testfieldwithmorethan70characters@Ithinkthisisalreadytoomuchbutitseems.ok',
                    integration_id='abc')
        with self.assertRaisesMessage(ValidationError,
                                      "{'email': ['Ensure this value has at most 70 characters (it has 73).']}"):
            user.full_clean()

    def test_integration_id_exceeded_max_length(self):
        user = User(name='test',
                    email='valid@email.com',
                    integration_id='testfieldwithmorethan70charactersIthinkthisisalreadytoomuchbutitseemsok')
        with self.assertRaisesMessage(ValidationError,
                                      "{'integration_id': ['Ensure this value has at most 70 characters (it has 71).']}"):
            user.full_clean()

    # Empty fields
    def test_email_should_not_be_empty(self):
        user = User(name='test', email='', integration_id='abc')
        with self.assertRaisesMessage(ValidationError, "{'email': ['This field cannot be blank.']}"):
            user.full_clean()

    def test_name_should_not_be_empty(self):
        user = User(email='valid@email.com', integration_id='abc')
        with self.assertRaisesMessage(ValidationError, "{'name': ['This field cannot be blank.']}"):
            user.full_clean()

    def test_integration_id_should_not_be_empty(self):
        user = User(name='test', email='valid@email.com', integration_id='')
        with self.assertRaisesMessage(ValidationError, "{'integration_id': ['This field cannot be blank.']}"):
            user.full_clean()

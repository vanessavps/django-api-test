from django.db import models
from django.core.validators import validate_email

class User(models.Model):
    # id field is auto generated
    name = models.CharField(max_length=70, blank=False)
    email = models.CharField(max_length=70, blank=False, validators=[validate_email])
    # assuming all users will have an integration_id
    integration_id = models.CharField(max_length=70, blank=False)

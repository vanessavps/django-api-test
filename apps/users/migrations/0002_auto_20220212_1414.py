# Generated by Django 4.0.2 on 2022-02-12 01:14

from django.db import migrations
from apps.users.models import User
from apps.users.data.dictionaries import user_dictionary


# Populate User table with users in dictionary
def populate_users(apps, schema_editor):
    for value in user_dictionary.values():
        # using **kwargs as the dictionary value has the same keywords as the model
        user = User(**value)
        user.save()

def delete_users(apps, schema_editor):
    for value in user_dictionary.values():
        User.objects.filter(id=value.id).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        # Populate users or delete users if need to rollback
        migrations.RunPython(populate_users, delete_users)
    ]

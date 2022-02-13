from rest_framework import serializers
from apps.users.models import User


# User serializer will return all User model fields
# Only name and email are editable but we still want to display integration_id on response
class UserSerializer(serializers.ModelSerializer):
    integration_id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'integration_id')

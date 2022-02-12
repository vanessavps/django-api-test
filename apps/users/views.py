from django.contrib.auth.models import User
from rest_framework import generics

from .models import User
from .serializers import UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

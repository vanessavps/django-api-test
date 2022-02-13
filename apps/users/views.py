from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.integrations.integration import update_user_external_system

from .models import User
from .serializers import UserSerializer


class UserDetail(APIView):
    # GET method
    # Returns user details given an id
    # If id not found an error message with 404 status will be returned
    def get(self, request, id):
        try:
            item = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error: User not found"}, status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(item)
        return Response(serializer.data, status.HTTP_200_OK)

    # PUT method
    # Updates user details given an id. It also updates details on external system
    # Returns updated object
    # If id not found an error message with 404 status will be returned
    def put(self, request, id):
        try:
            item = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error: User not found"}, status.HTTP_404_NOT_FOUND)

        # Partial is not accepted. The request data needs to have name and email
        # If name or email is missing an error message with 400 status will be returned
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            savedUser = serializer.save()
            update_user_external_system(savedUser)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)

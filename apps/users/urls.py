from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.users import views

urlpatterns = [
    path('settings/user/<int:id>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
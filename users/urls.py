from django.urls import path

from users.views import TestApi

urlpatterns = [
    path('check',TestApi.as_view()),
]

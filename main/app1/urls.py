from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.CreatePerson.as_view()),
]
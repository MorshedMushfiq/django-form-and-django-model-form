from django.urls import path
from FormApp.views import *


urlpatterns = [
    path('', formPage, name="formPage"),
]



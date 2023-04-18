from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('questions', questions_and_answers, name='questions'),
    path('rules', rules, name='rules'),
    path('contacts', contact, name='contacts'),
    path('en', index, name='english'),
    path('create', create, name='create'),
]

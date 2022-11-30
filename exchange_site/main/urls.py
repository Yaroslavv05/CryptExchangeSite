from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('questions', questions_and_answers, name='questions'),
    path('rules', rules, name='rules'),
    path('contacts', contact, name='contacts'),
    path('en', index, name='english'),
    path('create', create, name='create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

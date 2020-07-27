'''
    Created By Sara-Bolouri
    Created At 07-26-2020
'''
from django.urls import path
from .views import form_list

app_name = 'form_generator'

urlpatterns = [
    path('formlist/', form_list),
]
from django.urls import path
from .views import get_forms, create_new_form, delete_form, update_form

app_name = 'form_generator'

urlpatterns = [
    path('get/', get_forms, name='get_forms'),
    path('create/', create_new_form, name='create_form'),
    path('delete/<int:primary_key>/', delete_form, name='delete_form'),
    path('update/<int:primary_key>/', update_form, name='update_form')
]
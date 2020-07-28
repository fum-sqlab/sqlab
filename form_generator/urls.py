from django.urls import path
from .views import get_forms, create_new_form, delete_form, update_form, create_page

app_name = 'form_generator'

urlpatterns = [
    path('get/', get_forms, name='get_forms'),                          #http://127.0.0.1:8000/form/get/
    path('create/', create_new_form, name='create_form'),               #http://127.0.0.1:8000/form/create/
    path('delete/<int:primary_key>/', delete_form, name='delete_form'), #http://127.0.0.1:8000/form/delete/PK/
    path('update/<int:primary_key>/', update_form, name='update_form'), #http://127.0.0.1:8000/form/update/PK/
    path('create_page/', create_page, name='create_page')                #http://127.0.0.1:8000/page/create_page/
]
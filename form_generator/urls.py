from django.urls import path
from .views import *
                   

app_name = 'form_generator'

urlpatterns = [
    path('form/', FormView.as_view({'get':'list', 'post':'create'}) , name='get_create_forms'),
    path('form/<int:pk>/', FormView.as_view({'delete':'destroy', 'put':'update'}), name='delete_update_forms'),
    path('group/', GroupView.as_view({'get':'list', 'post':'create'}) , name='get_create_forms'),


    # path('create_page/', create_page, name='create_page'),
    # path('add_form/<int:page_pk>/<int:section_pk>/<int:form_pk>/', add_form, name='add_form'),
    # path('add_form_to_gp/<int:gp_pk>/<int:form_pk>/', add_form_to_group, name='add_form_to_gp')
]
from django.urls import path
from .views import *
                   

app_name = 'form_generator'

urlpatterns = [
    path('form/', FormView.as_view({'get':'list', 'post':'create'}) , name='get_create_form'),
    path('form/<int:pk>/', FormView.as_view({'delete':'destroy', 'put':'update', 'get':'show_form_details'}), name='delete_update_forms'),
    path('form/field_delete/<int:ff_id>/', FormView.as_view({'put':'add_field_to_form'}), name='set_field'),


    path('group/', GroupView.as_view({'get':'list', 'post':'create'}) , name='get_create_group'),
    path('group/<int:pk>/', GroupView.as_view({'delete':'destroy'}), name='delete_group'),
    path('group/<int:gp_pk>/<int:form_pk>/', GroupView.as_view({'put':'add_form_to_group', 'delete':'remove_form_from_group'}),
         name='set_remove_form'),
   
    path('page/', PageView.as_view({'get':'list', 'post':'create'}), name='get_create_page'),
    path('page/<int:pk>/', PageView.as_view({'delete':'destroy', 'get':'show_page_details'}), name='delete_page'),
    path('page/<int:page_pk>/<int:form_pk>/', PageView.as_view({'put':'add_form_to_page'}), name='set_form_to_page')
]
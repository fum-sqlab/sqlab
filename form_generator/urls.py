from django.urls import path
from .views import *
                   

app_name = 'form_generator'

urlpatterns = [
    path('form/', FormView.as_view({'get':'list', 'post':'create'}) , name='get_create_forms'),
    path('form/<int:pk>/', FormView.as_view({'delete':'destroy', 'put':'update'}), name='delete_update_forms'),
    path('group/', GroupView.as_view({'get':'list', 'post':'create'}) , name='get_create_forms'),
    path('set_group/<int:gp_pk>/<int:form_pk>/', GroupView.as_view({'post':'add_form_to_group'}), name='set_form_to_gp')
]
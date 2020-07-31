from .models import Form, Group, Page, Field
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

def get_form_object(primary_key):
    '''
        Retrive a specific object
    '''
    try:
        return Form.objects.get(pk=primary_key)
    except ObjectDoesNotExist:
        return None

def get_group_object(primary_key):
    '''
        Retrive a specific object
    '''
    try:
        return Group.objects.get(id=primary_key)
    except ObjectDoesNotExist:
        return None

def get_page_object(primary_key):
    '''
        Retrive a specific object
    '''
    try:
        return Page.objects.get(id=primary_key)
    except ObjectDoesNotExist:
        return None

def get_field_object(primary_key):
    '''
        Retrive a specific object
    '''
    try:
        return Field.objects.get(id=primary_key)
    except ObjectDoesNotExist:
        return None

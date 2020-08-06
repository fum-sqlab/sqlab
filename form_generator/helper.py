from .models import *
from .exception import exceptions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


TYPES = {
    "form" : Form,
    "field": Field,
    "page" : Page,
    "section" : Section,
    "group": Group,
    "formfield" : FormField,
    "pageform" : PageForm,
    "groupform" : GroupForm
}

def get_object(type_object="", primary_key=None):
    obj = TYPES[type_object]
    try:
        return obj.objects.get(pk=primary_key)
    except ObjectDoesNotExist:
        raise exceptions(type_object)

def filter_object(type_object="", **kwargs):
    obj = TYPES[type_object]
    result = obj.objects.filter(**kwargs).all()
    if not result.exists():
        raise exceptions(type_object)
    return result

def filter_for_deleting(type_object="", **kwargs):
    obj = TYPES[type_object]
    result = obj.objects.filter(**kwargs).all()
    if not result.exists():
        return None
    return result

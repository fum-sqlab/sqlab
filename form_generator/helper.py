from .models import *
from .exception import exceptions
from django.core.exceptions import ObjectDoesNotExist


TYPES = {
    "form" : Form,
    "field": Field,
    "page" : Page,
    "section" : Section,
    "group": Group,
    "formfield" : FormField,
    "pageform" : PageForm
}

def get_object(type_object=TYPES, primary_key=None):
    obj = TYPES[type_object]
    try:
        return obj.objects.get(pk=primary_key)
    except ObjectDoesNotExist:
        raise exceptions(type_object)

def filter_object(type_object="", **kwargs):
    obj = TYPES[type_object]
    # try:
    #     return obj.objects.filter(**kwargs).all()
    # except ObjectDoesNotExist:
    #     raise exceptions(type_object)
    resualt = obj.objects.filter(**kwargs).all()
    if not resualt.exists():
        raise exceptions(type_object)
    return resualt
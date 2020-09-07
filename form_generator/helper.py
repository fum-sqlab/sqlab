from .models import *
from .serializers import FormFieldSerializer, FieldSerializer, ChoiceSerializer
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
    "groupform" : GroupForm,
    "submission" : Submission,
    "choice" : Chioce
}

def get_object(type_object="", primary_key=None):
    obj = TYPES[type_object]
    try:
        return obj.objects.get(pk=primary_key)
    except ObjectDoesNotExist:
        raise exceptions(type_object)

def get_object_or_None(type_object="", primary_key=None):
    obj = TYPES[type_object]
    try:
        return obj.objects.get(pk=primary_key)
    except ObjectDoesNotExist:
        return None

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

def list_required_field(form_id):
    _fields = FormFieldSerializer(filter_object(type_object="formfield", form=form_id), many=True)
    required = []
    for item in _fields.data:
        if item["required"] == True:
            required.append(item["id"])   
    return required

def checking_requirement(requied_field, answers):
    '''
        If all required fields were answered by user, return TRUE else return FALSE
    '''
    for answer in answers:
        for rf in requied_field:
            if answer["field"] == rf:
                requied_field.remove(rf)
    return requied_field

def has_choice(fields_obj):
    fields_seri = FormFieldSerializer(fields_obj, many=True)
    _ids =[]
    for item in fields_seri.data:
        _id = item['field']
        obj = FieldSerializer(filter_object(type_object="field", id=_id), many=True)
        if obj.data[0]['field_type'] == "checkbox" or obj.data[0]['field_type'] == "radio":
            return True
    
    return False

def get_items(_id):
    objs = filter_for_deleting(type_object="choice", field=_id)
    items = []
    if objs is not None:
        obj_seri = ChoiceSerializer(objs, many=True)
        for item in obj_seri.data:
            items.append({"id":item["id"], "name":item["name"]})
    return items

def get_field_type(_id):
    field = get_object(type_object="field", primary_key=_id)
    field_seri = FieldSerializer(field)
    return field_seri.data.get("field_type")

def remove_repeated_id(_ids):
    repeated_id = []
    for _id in _ids:
        if _id not in repeated_id:
            repeated_id.append(_id)
    
    return repeated_id
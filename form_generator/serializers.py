'''
    Created By Sara-Bolouri
    Created At 07-26-2020
'''
from rest_framework import serializers
from .models import Form, Field, FormField

class FieldSerializer(serializers.ModelSerializer): 
    '''
        Field Serializers Model
    '''
    class Meta:
        model = Field
        field = ['id', 'name', 'label', 'field_type',
                 'description', 'help_text', 'min_val',
                 'max_val', 'default_val', 'required',
                 'visible', 'enable']

class FormFieldSeializer(serializers.ModelSerializer):
    '''
        Many-To-Many relationships between Form and Field
    '''
    field = serializers.PrimaryKeyRelatedField(queryset=Field.objects.all())
    form = serializers.PrimaryKeyRelatedField(queryset=Form.objects.all())

    class Meta:
        model = FormField
        field = ['id', 'field', 'form']

class FormSerializer(serializers.ModelSerializer):
    '''
        Form Serializers Model
    '''
    fields = FieldSerializer(many=True, read_only=True)
    class Meta:
        model = Form
        field = ['id', 'title', 'description', 'fields',
                 'visible', 'enable', 'created_by',
                 'updated_by']

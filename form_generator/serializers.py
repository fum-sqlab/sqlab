'''
    Created By Sara-Bolouri
    Created At 07-26-2020
'''
from rest_framework import serializers
from .models import *
from django.core.exceptions import ObjectDoesNotExist


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):
    fields = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Form
        fields = '__all__'

    def create(self, valide_data):
        return Form.objects.create(**valide_data)

    def update(self, instance, new_valid_data):

        all_fields = new_valid_data.get('fields')
        instance.title = new_valid_data.get('title')
        instance.description = new_valid_data.get('description')
        instance.visible = new_valid_data.get('visible')
        instance.enable = new_valid_data.get('enable')
        instance.created_by = new_valid_data.get('created_by')
        instance.updated_by = new_valid_data.get('updated_by')
        instance.save()

        for field in all_fields:
            field_id = field.get('id')
            try:
                field_obj = Field.objects.get(pk=field_id)
            except Field.DoesNotExist:
                pass

            field_obj.name = field.get('name')
            field_obj.label = field.get('label')
            field_obj.description = field.get('description')
            field_obj.help_text = field.get('help_text')
            field_obj.field_type = field.get('field_type')
            field_obj.min_value = field.get('min_value')
            field_obj.max_value = field.get('max_value')
            field_obj.default_value = field.get('default_value')
            field_obj.required = field.get('required')
            field_obj.enable = field.get('enable')
            field_obj.visible = field.get('visible')
            field_obj.save()
        
        return instance

class GroupSerializer(serializers.ModelSerializer):
    form = FormSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validate_data):
        return Section.objects.create(**validate_data)

class PageSerializer(serializers.ModelSerializer):
    forms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Page
        fields = '__all__'

    def create(self, valide_data):
        return Page.objects.create(**valide_data)

class PageFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageForm
        fields = '__all__'

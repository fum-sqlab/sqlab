'''
    Created By Sara-Bolouri
    Created At 07-26-2020
'''
from rest_framework import serializers
from .models import Form, Field, Page, Section, Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
    
class FieldSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Field
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)
    groups = GroupSerializer(many=True, required=False)
    class Meta:
        model = Form
        fields = '__all__'
        

    def create(self, valide_data):
        '''
            Create new Form object and add all Fields object to this form
            ----------------------------------------------------------------------------------------
            Step1: POP fields key/value
            Step2: Create new Form Object
            Step3: Create new Field object for each field that was created by User. then save it.
            Step4: Add List of filed objects to form object
            step5: Save form object. 
            ----------------------------------------------------------------------------------------
        '''
        all_fields = valide_data.pop('fields')
        form = Form.objects.create(**valide_data)
        fields = []
        for field in all_fields:
            new_field = Field(**field)
            new_field.save()
            fields.append(new_field)
        form.fields.add(*fields)    
        form.save()
        return form

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

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    forms = FormSerializer(many=True)
    sections = SectionSerializer(many=True)
    class Meta:
        model = Page
        fields = '__all__'

    def create(self, valide_data):
        all_forms = valide_data.pop('forms')
        all_sections = valide_data.pop('sections')
        page = Page.objects.create(**valide_data)
        lst = []
        for form in all_forms:
            new_form = Form(**form)
            new_form.save()
            lst.append(new_form)
        page.forms.add(*lst)
        lst.clear()
        for section in all_sections:
            new_sec = Section(**section)
            new_sec.save()
            lst.append(new_sec)
        page.sections.add(*lst)
        page.save()
        return page



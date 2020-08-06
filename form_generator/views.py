'''
    Created By Sara-Bolouri
    Created At 07-25-2020
'''
from form_generator.models import *
from form_generator.serializers import *
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .helper import *
from .exception import exceptions
from .status import *

class FormView(viewsets.ViewSet):

    def list(self, request):
        '''
            Get all Forms
        '''
        forms = Form.objects.all()
        forms_serializer = FormSerializer(forms, many=True)
        return Response(forms_serializer.data, status=SUCCEEDED_REQUEST)

    def create(self, request):
        '''
            Create new Form Object
        '''
        form_data = request.data
        all_fields = form_data.pop('fields')
        form = FormSerializer(data=form_data)
        if form.is_valid():
            form.save()
            for field in all_fields:
                field['field'] = field.pop('field_id')
                field['form'] = form.data.get('id')
                new_record = FormFieldSerializer(data=field)
                if new_record.is_valid():
                    new_record.save()
                else:
                    return Response(new_record.errors, status=INVALID_DATA)
        else:
            return Response(form.errors, status=INVALID_DATA)

        return Response("The New Form Created.", status=CREATED)
    
    def destroy(self, request, pk=None):
        '''
            Delete form object that its 'id' is 'pk'
        '''
        form = get_object(type_object="form", primary_key=pk)
        filter_object(type_object="formfield", form=pk).all().delete()
        filter_object(type_object="pageform", form=pk).all().delete()
        form.delete()
        return Response(status=DELETED)

    #Havenot tested yet
    def update(self, request, pk=None):
        '''
            Update form object that its 'id' is 'pk'
        '''
        form = get_object(type_object="form", primary_key=pk)
        updated_form = FormSerializer(form, data=request.data)
        if updated_form.is_valid():
            updated_form.save()
            return Response(updated_form.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PUT'])
    def add_field_to_form(self, request, field_pk, form_pk):
        details = request.data
        details['field'] = field_pk
        details['form'] = form_pk
        form_field_seri = FormFieldSerializer(data=details)
        if form_field_seri.is_valid():
            form_field_seri.save()
            return Response(form_field_seri.data, status=SUCCEEDED_REQUEST)
        return Response(form_field_seri.errors, status=INVALID_DATA)

    @action(detail=True, methods=['DELETE'])
    def remove_field_from_form(self, request, ff_id):
        result = filter_for_deleting(type_object="formfield", id=ff_id)
        if result is not None:
            result.delete()
        return Response(status=DELETED)

    @action(detail=True, methods=['GET'])
    def show_form_details(self, request, pk=None):
        form_seri = FormSerializer(get_object(type_object="form", primary_key=pk)).data
        form_field_seri = FormFieldSerializer(filter_object(type_object="formfield", form=pk), many=True)
        
        for field in form_field_seri.data:
            field_id = field.pop('field')
            field_seri = FieldSerializer(get_object(type_object="field", primary_key=field_id))
            field_type = field_seri.data.get('field_type')
            field["field_type"] = field_type

        form_seri['fields'] = form_field_seri.data
        return Response(form_seri, status=SUCCEEDED_REQUEST)
        
class GroupView(viewsets.ViewSet):

    def list(self, request):
        '''
            Get all groups
        '''
        groups = Group.objects.all()
        groups_serializer = GroupSerializer(groups, many=True)
        return Response(groups_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        '''
            Create a new group
        '''
        group_serializer = GroupSerializer(data=request.data)
        if group_serializer.is_valid():
            group_serializer.save()
            return Response(group_serializer.data, status=CREATED)
        return Response(group_serializer.errors, status=INVALID_DATA)

    def destroy(self, request, pk):
        '''
            Delete a group
        '''
        result = filter_for_deleting(type_object="groupform", group=pk)
        if result is not None:
            result.delete()
        get_object(type_object="group", primary_key=pk).delete()
        return Response(status=DELETED)

    def retrive(self, request, pk):
        gp = get_object(type_object="group", primary_key=pk)
        gp_serializer = GroupSerializer(gp)
        return Response(gp_serializer.data, status=SUCCEEDED_REQUEST)

    @action(detail=True, methods=['PUT'])
    def add_form_to_group(self, request, gp_pk, form_pk):
        '''
            Set a form to a specific group
        '''
        form = get_object(type_object="form", primary_key=form_pk)
        group = get_object(type_object="group", primary_key=gp_pk)
        
        group.form.add(*[form])
        group.save()
        return Response("ok", status=SUCCEEDED_REQUEST)  
         
    @action(detail=True, methods=['DELETE'])
    def remove_form_from_group(self, request, gp_pk, form_pk):
        '''
            Remove a from from list of specific group
        '''
        result = filter_for_deleting(type_object="groupform", form=form_pk, group=gp_pk)
        if result is not None:
            result.delete()
            return Response(status=DELETED)
        return Response("No data", status=NOT_FOUND)

class PageView(viewsets.ViewSet):

    def list(self, request):
        '''
            Show all pages
        '''
        pages = Page.objects.all()
        pages_serializer = PageSerializer(pages, many=True)
        return Response(pages_serializer.data, status=SUCCEEDED_REQUEST)

    def create(self, request):
        '''
            Create new page
        '''
        page_data = request.data
        forms = page_data.pop('forms')
        page = PageSerializer(data=page_data)
        if page.is_valid():
            page.save()
        else:
            return Response(page.errors, status=INVALID_DATA)

        for form in forms:
            section_data = {
                "title" : form["section_name"],
                "slug"  : form["slug"],
                "placeholder" : form["placeholder"]
            }
            section = SectionSerializer(data=section_data)
            if section.is_valid():
                section.save()
            else:
                return Response(status=400)
            
            pageForm_details = {
                "page" : page.data["id"],
                "form" : form["id"],
                "section" : section.data["id"]
            }

            pageform = PageFormSerializer(data=pageForm_details)
            if pageform.is_valid():
                pageform.save()
            else:
                return Response(pageform.errors, status=INVALID_DATA)

        return Response("Done",status=SUCCEEDED_REQUEST)
        
    def destroy(self, request, pk=None):
        page = Page.objects.get(pk=pk)
        result = filter_for_deleting(type_object="pageform", page=pk)
        if result is not None:
            result.delete()
        page.delete()
        return Response(status=SUCCEEDED_REQUEST)

    @action(detail=True, methods=['PUT'])
    def add_form_to_page(self, request, page_pk, form_pk):
        section_serializer = SectionSerializer(data=request.data)
        if section_serializer.is_valid():
            section_serializer.save()
            pageform_data = {
                "form" : form_pk,
                "page" : page_pk,
                "section" : section_serializer.data["id"]
            }
            pageform = PageFormSerializer(data=pageform_data)
            if pageform.is_valid():
                pageform.save()
                msg = {"message":"Done"}
                stu = status.HTTP_200_OK
            else:
                msg = pageform.errors
                stu = status.HTTP_400_BAD_REQUEST            
        else:
            msg = section_serializer.errors
            stu = status.HTTP_400_BAD_REQUEST 
        return Response(msg, status=stu) 
            
    @action(detail=True, methods=['DELETE'])
    def remove_form_from_page(self, request, page_pk, form_pk, section_pk):
        filter_object(type_object="pageform", form=form_pk, page=page_pk, section=section_pk).delete()
        get_object(type_object="section", primary_key=section_pk).delete()
        return Response("ok", status=200)
        
    @action(detail=True, methods=['GET'])
    def show_page_details(self, request, pk=None):
        page = PageSerializer(get_object(type_object="page", primary_key=pk)).data
        forms_id = page.pop("forms")
        print(page)
        forms = []
        for form_id in forms_id:
            form = FormSerializer(get_object(type_object="form", primary_key=form_id)).data
            form_field = filter_object(type_object="formfield", form=form_id)
            form_field_data = FormFieldSerializer(form_field, many=True) #all form fields
            fields = []
            for field in form_field_data.data:
                field.pop("form")
                id = field.pop("field")
                field_type = FieldSerializer(get_object(type_object="field", primary_key=id)).data["field_type"]
                field["field_type"] = field_type
                fields.append(field)
            form["fields"] = fields
            forms.append(form)
        page["forms"] = forms

        return Response(page, status=200)
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
from django.core.exceptions import ObjectDoesNotExist


class FormView(viewsets.ViewSet):

    def list(self, request):
        '''
            Get all Forms
        '''
        forms = Form.objects.all()
        forms_serializer = FormSerializer(forms, many=True)
        return Response(forms_serializer.data, status=200)

    def create(self, request):
        '''
            Create new Form Object
        '''
        form_data = request.data
        all_fields = form_data.pop('fields')
        form = FormSerializer(data=form_data)
        if form.is_valid():
            form.save()
        else:
            return Response(form.errors, status=404)

        for field in all_fields:
            field['field'] = field.pop('field_id')
            field['form'] = form.data.get('id')
            new_record = FormFieldSerializer(data=field)
            if new_record.is_valid():
                new_record.save()
            else:
                return Response(new_record.errors)
        return Response("Done", status=200)
    
    def destroy(self, request, pk=None):
        '''
            Delete form object that its 'id' is 'pk'
        '''
        print('here-------------------------------------------------------------------------------------')
        form = get_form_object(primary_key=pk)
        if form is not None:
            try:
                FormField.objects.filter(form=pk).all().delete()
            except ObjectDoesNotExist:
                pass
            try:
                PageForm.objects.filter(form=pk).all().delete()
            except ObjectDoesNotExist:
                pass
            form.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"Error":"Form doesn't find"}, status=404)

    def update(self, request, pk=None):
        '''
            Update form object that its 'id' is 'pk'
        '''
        form = get_form_object(primary_key=pk)
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
            return Response(form_field_seri.data, status=200)
        return Response(form_field_seri.errors, status=400)

    @action(detail=True, methods=['DELETE'])
    def remove_field_from_form(self, request, ff_id):
        try:
            FormField.objects.filter(id=ff_id).delete()
            return Response({"message":"Done"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message":"No data"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['GET'])
    def show_form_details(self, request, pk=None):
        try:
            form_obj = Form.objects.get(pk=pk)
            form_seri = FormSerializer(form_obj).data
            form_field_obj = FormField.objects.filter(form=pk)
            form_field_seri = FormFieldSerializer(form_field_obj, many=True)
        except ObjectDoesNotExist:
            return Response({"Error": "Dosn't found Object"}, status=404)
        
        for field in form_field_seri.data:
            field_id = field.pop('field')
            try:
                field_obj = Field.objects.get(pk=field_id)
                field_seri = FieldSerializer(field_obj)
                field_type = field_seri.data.get('field_type')
                field["field_type"] = field_type
            except ObjectDoesNotExist:
                return Response({"Error": "Doesn't found field"},status=404)

        form_seri['fields'] = form_field_seri.data
        return Response(form_seri, status=200)
        
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
            return Response(group_serializer.data, status=status.HTTP_201_CREATED)
        return Response(group_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        '''
            Delete a group
        '''
        group = get_group_object(primary_key=pk)
        group.delete()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['PUT'])
    def add_form_to_group(self, request, gp_pk, form_pk):
        '''
            Set a form to a specific group
        '''
        form = get_form_object("Form", primary_key=form_pk)
        group = get_group_object("Group", primary_key=gp_pk)
        if form is None:
            msg = {"message":"This form doesn't exist"}
            stu = status.HTTP_400_BAD_REQUEST
        elif group is None:
            msg = {"message":"This group doesn't exist"}
            stu = status.HTTP_400_BAD_REQUEST
        else:
            msg = {}
            stu = status.HTTP_200_OK
            lst = [form]
            group.form.add(*lst)
            group.save()
        return Response(msg, status=stu)  
         
    @action(detail=True, methods=['DELETE'])
    def remove_form_from_group(self, request, gp_pk, form_pk):
        '''
            Remove a from from list of specific group
        '''
        try:
            GroupForm.objects.filter(form=form_pk, group=gp_pk).delete()
            return Response({"message":"Done"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message":"No data"}, status=status.HTTP_404_NOT_FOUND)

class PageView(viewsets.ViewSet):

    def list(self, request):
        '''
            Show all pages
        '''
        pages = Page.objects.all()
        pages_serializer = PageSerializer(pages, many=True)
        return Response(pages_serializer.data, status=status.HTTP_200_OK)

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
            return Response(page.errors, status=400)

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
                return Response(status=404)

        return Response("Done",status=200)
            
        # page_serializer = PageSerializer(data=request.data)
        # if page_serializer.is_valid():
        #     page_serializer.save()
        #     return Response(page_serializer.data, status=status.HTTP_201_CREATED)
        # return Response(page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        page = Page.objects.get(pk=pk)
        try:
            PageForm.objects.filter(page=pk).all().delete()
        except ObjectDoesNotExist:
            pass
        page.delete()
        return Response(status=status.HTTP_200_OK)

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
        try:
            PageForm.objects.filter(form=form_pk, page=page_pk, section=section_pk).delete()
            return Response("deleted", status=200)
        except ObjectDoesNotExist:
            return Response("doesn't exist", status=404)
        
    # @action(detail=True, methods=['GET'])
    # def show_page_details(self, request, pk=None):
    #     page = Page.objects.get(pk=pk)
    #     page_serializer = PageSerializer(page)
    #     forms_id = page_serializer.data.pop("forms")
    #     for form in form_id:




    #     return Response("ok")
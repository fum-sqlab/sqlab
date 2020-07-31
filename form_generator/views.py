'''
    Created By Sara-Bolouri
    Created At 07-25-2020
'''
from form_generator.models import *
from form_generator.serializers import FormSerializer, PageSerializer, SectionSerializer, GroupSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
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
        return Response(forms_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        '''
            Create new Form Object
        '''
        form_serializer = FormSerializer(data=request.data)
        if form_serializer.is_valid():
            form_serializer.save()
            return Response(form_serializer.data, status=status.HTTP_201_CREATED)
        return Response(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        '''
            Delete form object that its 'id' is 'pk'
        '''
        form = get_form_object(primary_key=pk)
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
        form = get_form_object(primary_key=form_pk)
        field = get_field_object(primary_key=field_pk)

        if form is None:
            msg = {"message":"This form doesn't exist"}
            stu = status.HTTP_400_BAD_REQUEST
        elif field is None:
            msg = {"message":"This field doesn't exist"}
            stu = status.HTTP_400_BAD_REQUEST
        else:
            form.fields.add(*[field])
            form.save()
            msg = {"message":"Done"}
            stu = status.HTTP_200_OK
        return Response(msg, status=stu)

    @action(detail=True, methods=['DELETE'])
    def remove_field_from_form(self, request, field_pk, form_pk):
        try:
            FormField.objects.filter(form=form_pk, field=field_pk).delete()
            return Response({"message":"Done"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message":"No data"}, status=status.HTTP_404_NOT_FOUND)

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
    def remove_form_from_grou(self, request, gp_pk, form_pk):
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
        page_serializer = PageSerializer(data=request.data)
        if page_serializer.is_valid():
            page_serializer.save()
            return Response(page_serializer.data, status=status.HTTP_201_CREATED)
        return Response(page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        page = Page.objects.get(pk=pk)
        page.delete()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['PUT'])
    def add_form_to_page(self, request, page_pk, form_pk):
        page = get_page_object(primary_key=page_pk)
        form = get_form_object(primary_key=form_pk)
        if form is None:
            msg = {"message":"This form doesn't exist"}
            stu = status.HTTP_400_BAD_REQUEST
        elif page is None:
            msg = {"message":"This page doesn't exist"}
            stu = status.HTTP_400_BAD_REQUEST
        else:
            page.forms.add(*[form])
            print(page)
            section_serializer = SectionSerializer(data=request.data)
            if section_serializer.is_valid():
                section_obj = section_serializer.save()
                page.sections.add(*[section_obj])
                page.save()
                msg = {"message":"Done"}
                stu = status.HTTP_200_OK
            else:
                msg = section_serializer.errors
                stu = status.HTTP_400_BAD_REQUEST 
        return Response(msg, status=stu)

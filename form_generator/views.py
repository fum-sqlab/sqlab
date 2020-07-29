'''
    Created By Sara-Bolouri
    Created At 07-25-2020
'''
from form_generator.models import Form, Page, Section, Group, GroupForm
from form_generator.serializers import FormSerializer, PageSerializer, SectionSerializer, GroupSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .helper import get_group_object, get_form_object


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

class GroupView(viewsets.ViewSet):

    def list(self, request):
        groups = Group.objects.all()
        groups_serializer = GroupSerializer(groups, many=True)
        return Response(groups_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        group_serializer = GroupSerializer(data=request.data)
        if group_serializer.is_valid():
            group_serializer.save()
            return Response(group_serializer.data, status=status.HTTP_201_CREATED)
        return Response(group_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PUT'])
    def add_form_to_group(self, request, gp_pk, form_pk):
        '''
            Set a form to a specific group
        '''
        form = get_form_object(primary_key=form_pk)
        group = get_group_object(primary_key=gp_pk)
        lst = [form]
        group.form.add(*lst)
        group.save()
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['PUT'])
    def remove_form_from_grou(self, request, gp_pk, form_pk):
        try:
            GroupForm.objects.filter(form=form_pk, group=gp_pk).delete()
            return Response({"message":"Done"}, status=status.HTTP_200_OK)
        except GroupForm.DoesNotExist:
            return Response({"message":"No data"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def create_page(request):
    page_serializer = PageSerializer(data=request.data)
    if page_serializer.is_valid():
        page_serializer.save()
        return Response(page_serializer.data, status=status.HTTP_200_OK)
    return Response(page_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_section(request):
    section_serializer = SectionSerializer(data=request.data)
    if section_serializer.is_valid():
        section_serializer.save()
        return Response(section_serializer.data, status=status.HTTP_201_CREATED)
    return Response(section_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def add_form(request, page_pk, section_pk, form_pk):
    try:
        page = Page.objects.get(pk=page_pk)
        form = Form.objects.get(pk=form_pk)
        section = Section.objects.get(pk=section_pk)
    except Page.DoesNotExist or Form.DoesNotExist or Section.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    lst =[]
    lst.append(form)
    page.forms.add(*lst)
    lst.clear()
    lst.append(section)
    page.sections.add(*lst)
    page.save()
    return Response(page, status=status.HTTP_200_OK)
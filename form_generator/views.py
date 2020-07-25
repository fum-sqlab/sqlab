'''
    Created By Sara-Bolouri
    Created At 07-25-2020
'''
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from form_generator.models import Form
from form_generator.serializers import FormSerializer

def get_object(request, primary_key):
    '''
        Retrive a specific object
    '''
    try:
        return Form.objects.get(pk=primary_key)
    except Form.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def form_list(request):
    '''
        List all Forms, or Create a new Form
    '''
    if request.method == 'GET':
        forms = Form.objects.all()
        form_serializer = FormSerializer(forms, many=True)
        return Response(form_serializer.data)

    elif request.method == 'POST':
        form_serializer = FormSerializer(data=request.data)
        if form_serializer.is_valid:
            form_serializer.save()
            return Response(form_serializer.data, status=status.HTTP_201_CREATED)
        return Response(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_specific_form(request, primary_key):
    '''
        Retrive a specific form
    '''
    form = get_object(request, primary_key)
    if request.method == 'GET':
        form_serializer = FormSerializer(form, many=True)
        return Response(form_serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_specific_form(request, primary_key):
    '''
        Update a specific form
    '''
    form = get_object(request, primary_key)
    if request.method == 'PUT':
        updated_form = FormSerializer(form, data=request.data)
        if updated_form.is_valid:
            updated_form.save()
            return Response(updated_form.data)
        return Response(updated_form.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_specific_form(request, primary_key):
    '''
        Delete a specific form
    '''
    form = get_object(request, primary_key)
    if request.method == 'DELETE':
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

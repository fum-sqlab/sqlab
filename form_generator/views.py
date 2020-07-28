'''
    Created By Sara-Bolouri
    Created At 07-25-2020
'''
from form_generator.models import Form
from form_generator.serializers import FormSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_object(primary_key):
    '''
        Retrive a specific object
    '''
    try:
        return Form.objects.get(pk=primary_key)
    except Form.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_forms(requesrt):
    if requesrt.method == 'GET':
        forms = Form.objects.all()
        forms_serializer = FormSerializer(forms, many=True)
        return Response(forms_serializer.data, status=status.HTTP_200_OK)   

@api_view(['POST'])
def create_new_form(requesrt):
    form_serializer = FormSerializer(data=request.data)
    if form_serializer.is_valid:
        form_serializer.save()
        return Response(form_serializer.data, status=status.HTTP_201_CREATED)
    return Response(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

@api_view(['DELETE'])
def delete_form(requesrt, primary_key):
    form = get_object(primary_key=primary_key)
    form.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  
                
@api_view(['PUT'])
def update_form(requesrt, primary_key):
    form = get_object(primary_key=primary_key)
    updated_form = FormSerializer(form, data=requesrt.data)
    if updated_form.is_valid():
        updated_form.save()
        return Response(updated_form.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    
    
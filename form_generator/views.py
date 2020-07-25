'''
    Created By Sara-Bolouri
    Created At 07-25-2020
'''
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from form_generator.models import Form
from form_generator.serializers import FormSerializer

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
        Retrive a specifi form
    '''
    try:
        form = Form.objects.get(pk=primary_key)
    except Form.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        form_serializer = FormSerializer(form, many=True)
        return Response(form_serializer.data, status=status.HTTP_200_OK)
        
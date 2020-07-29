from .models import Form, Group


def get_form_object(primary_key):
    '''
        Retrive a specific object
    '''
    try:
        return Form.objects.get(pk=primary_key)
    except Form.DoesNotExist:
        return Response({"message":"This form doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

def get_group_object(primary_key):
    try:
        return Group.objects.get(pk=primary_key)
    except Group.DoesNotExist:
        return Response({"message":"This group doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
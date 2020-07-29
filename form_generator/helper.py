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
        group = Group.objects.get(pk=primary_key)
    except Group.DoesNotExist or Form.DoesNotExist:
        return Response({"message":"This group doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
# import uuid
# from django.db import models
# from users.models import User
#
#
# class UserProfile(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     first_name = models.CharField(max_length=50, unique=False)
#     last_name = models.CharField(max_length=50, unique=False)
#     phone = models.CharField(max_length=11, unique=True, null=False, blank=False)
#
#     class Meta:
#         '''
#         to set table name in database
#         '''
#         db_table = "profile"

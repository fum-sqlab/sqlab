from django.contrib.auth.models import Group
from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
# from profile.models import UserProfile
from users.models import User

#new
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
#

#new
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'phone')
#


#new
class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required=False)

    class Meta:
        model = User
        # fields = ('email', 'password', 'profile')
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create_user(**validated_data)
        # UserProfile.objects.create(
        #     user=user,
        #     first_name=profile_data['first_name'],
        #     last_name=profile_data['last_name'],
        #     phone_number=profile_data['phone_number'],
        # )
        # return user
#

#new
class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        # user,email,password validator

        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }
#

#class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CustomUser
#         fields = ('email', 'username', 'url',)


##need to be tested
#class GroupSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Group
        #fields = ['url', 'name']
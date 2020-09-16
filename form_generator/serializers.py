'''
    Created By Sara-Bolouri
    Created At 07-26-2020
'''
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username'] 

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chioce
        fields = '__all__'

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):
    fields = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Form
        fields = '__all__'

    def create(self, valide_data):
        return Form.objects.create(**valide_data)

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validate_data):
        return Section.objects.create(**validate_data)

class PageSerializer(serializers.ModelSerializer):
    forms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Page
        fields = '__all__'

    def create(self, valide_data):
        return Page.objects.create(**valide_data)

class PageFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageForm
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Submission
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chioce
        fields = '__all__'
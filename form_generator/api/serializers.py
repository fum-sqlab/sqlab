from rest_framework import serializers
from ..models import Form, Field, Form_Field

class FieldSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    label = serializers.CharField(max_length=50)
    field_type = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=1000)
    help_text = serializers.CharField(max_length=1000)
    min_val = serializers.CharField(max_length=50, default=None)
    max_val = serializers.CharField(max_length=50, default=None)
    default_val = serializers.CharField(max_length=50, default=None)
    required = serializers.BooleanField(default=False)
    visible = serializers.BooleanField(default=True)
    enable = serializers.BooleanField(default=True)


class FormSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=1000)
    visible = serializers.BooleanField(default=True)
    enable = serializers.BooleanField(default=True)
    created_by = serializers.CharField(max_length=50)
    updated_by = serializers.CharField(max_length=50)
    fields = FieldSerializer(many=True, read_only=True)



from django.db import models

# Create your models here.

class Form(models.Model):
    '''
    Model for each Form
    '''
    id = models.BigAutoField(unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    fields = models.ManyToManyField('Field', through='Form_Field')
    visible = models.BooleanField(default=True)
    enable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    updated_by = models.ForeignKey('User', on_delete=models.SET_NULL,
                                   null=True, blank=True)


class Field(models.Model):
    '''
    Model For each data field
    '''
    id = models.BigAutoField(unique=True)
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)
    help_text = models.TextField(max_length=200)
    type = models.CharField(default=None, max_length=50)
    min_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    max_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    default_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    required = models.BooleanField(default=False)
    enable = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)

class Form_Field(models.Model):
    '''
    Model for connection between Form and Field table
    '''
    id = models.BigAutoField(primary_key = True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    name = models.CharField(default=None, null=True, blank=True, max_length=50)
    label = models.CharField(default=None, null=True, blank=True,max_length=50)
    description = models.CharField(default=None, max_length=100, null=True, blank=True)
    help_text = models.TextField(default=None, null=True, blank=True, max_length=200)
    min_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    max_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    default_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    placeHolder = models.CharField(max_length=100)
    required = models.BooleanField(default=None, null=True, blank=True)
    enable = models.BooleanField(default=None, null=True, blank=True)
    visible = models.BooleanField(default=None, null=True, blank=True)

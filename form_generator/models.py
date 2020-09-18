'''
    Created By Sara-Bolouri
    Created At 07-26-2020
'''
from django.db import models
from django.contrib.auth.models import User



class Field(models.Model):
    '''
    Model For each data field
    '''
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    help_text = models.CharField(max_length=2000, null=True, blank=True)
    field_type = models.CharField(max_length=100)

class Form(models.Model):
    '''
    Model for each Form
    '''
    slug = models.SlugField(max_length=100, unique=True, default=None)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    fields = models.ManyToManyField(Field, through="FormField", related_name="fields")
    visible = models.BooleanField(default=True)
    enable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   null=True, blank=True, related_name='form_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   null=True, blank=True, related_name='form_updated_by')

class FormField(models.Model):
    '''
    Model for connection between Form and Field table
    '''
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    name = models.CharField(default=None, null=True, blank=True, max_length=50)
    label = models.CharField(default=None, null=True, blank=True,max_length=50)
    description = models.CharField(default=None, max_length=100, null=True, blank=True)
    min_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    max_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    default_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    placeHolder = models.CharField(max_length=100, null=True, blank=True,)
    required = models.BooleanField(default=False, null=True, blank=True)
    enable = models.BooleanField(default=True, null=True, blank=True)
    visible = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        ordering = ['form_id']

class Chioce(models.Model):
    field = models.ForeignKey(FormField, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Page(models.Model):
    '''
    Model fot Page
    '''
    slug = models.SlugField(max_length=100, unique=True)
    forms = models.ManyToManyField('Form', through='PageForm', related_name='forms')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True, blank=True)
    text_body = models.CharField(default=None, max_length=1000, null=True, blank=True)
    enable = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   blank=True, null=True, related_name='page_created_by')
    update_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   blank=True, null=True, related_name='page_updated_by')

class Section(models.Model):
    '''
    Model for Section. It is a place in which holding a page.
    '''
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    placeholder = models.CharField(max_length=100)

class PageForm(models.Model):
    '''
    Model for connection between a form and section a page. these should be unique
    '''
    page = models.ForeignKey('Page', on_delete=models.DO_NOTHING)
    form = models.ForeignKey('Form', on_delete=models.DO_NOTHING)
    section = models.ForeignKey('Section', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('page', 'form', 'section')

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    page = models.ForeignKey('Page', on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    submission = models.ForeignKey('Submission', on_delete=models.CASCADE)
    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    field = models.ForeignKey('FormField', on_delete=models.CASCADE)
    value = models.CharField(default=None, max_length=200)

class File(models.Model):
    file = models.FileField(blank=True, null=True)
    value = models.ForeignKey('Answer', on_delete=models.CASCADE)
    def __str__(self):
        return self.file.name
from django.db import models
from django.contrib.auth.models import User


class Form(models.Model):
    '''
    Model for each Form
    '''
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    fields = models.ManyToManyField('Field', through='Form_Field')
    visible = models.BooleanField(default=True)
    enable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='form_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='form_updated_by')

    def __str__(self):
        return self.title

class Field(models.Model):

    '''
    Model For each data field
    '''
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=2000, null=True, blank=True)
    help_text = models.CharField(max_length=2000)
    field_type = models.CharField(max_length=100)
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
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
    # order = models.IntegerField(null=True, blank=True)
    # name = models.CharField(default=None, null=True, blank=True, max_length=50)
    # label = models.CharField(default=None, null=True, blank=True,max_length=50)
    # description = models.CharField(default=None, max_length=100, null=True, blank=True)
    # help_text = models.TextField(default=None, null=True, blank=True, max_length=200)
    # min_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    # max_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    # default_value = models.CharField(default=None, null=True, blank=True, max_length=50)
    # placeHolder = models.CharField(max_length=100)
    # required = models.BooleanField(default=None, null=True, blank=True)
    # enable = models.BooleanField(default=None, null=True, blank=True)
    # visible = models.BooleanField(default=None, null=True, blank=True)

class Page(models.Model):
    '''
    Model fot Page
    '''
    slug = models.SlugField(max_length=100, unique=True)
    forms = models.ManyToManyField('Form', through='Page_Form')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True, blank=True)
    text_body = models.CharField(default=None, max_length=1000, null=True, blank=True)
    enable = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='page_created_by')
    update_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='page_updated_by')

class Section(models.Model):
    '''
    Model for Section. It is a place in which holding a page.
    '''
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    placeholder = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='section_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='section_updated_by')

class Page_Form(models.Model):
    '''
    Model for connection between a form and section a page. these should be unique
    '''
    page = models.ForeignKey('Page', on_delete=models.CASCADE)
    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('page', 'form', 'section')

class Group(models.Model):
    '''
    Model for group of form
    '''
    gp_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    form = models.ManyToManyField('Form', through='Group_Form')
    permissions = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='group_created_by')
    updated_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='group_updated_by')

    class Meta:
        verbose_name = 'Fields\' Group'

class Group_Form(models.Model):
    '''
    Model for connection between Group and Form.
    '''
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    form = models.ForeignKey('Form', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('group', 'form')

class History(models.Model):
    '''
    Model for a history. each form can have many versions of history.
    '''
    form_data = models.ForeignKey('Form_Field', on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey('Answer', on_delete=models.SET_NULL, null=True)
    history_info = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    page = models.ForeignKey('Page_Form', on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    submission = models.ForeignKey('Submission', on_delete=models.CASCADE)
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    value = models.CharField(default=None, max_length=200)






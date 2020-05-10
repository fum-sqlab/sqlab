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
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, null=True)
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


class Page(models.Model):
    '''
    Model fot Page
    '''
    id = models.AutoField(primaey_key=True)
    slug = models.SlugField(max_length=100, unique=True)
    forms = models.ManyToManyField('Form', through='Page_Form')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True, blank=True)
    text_body = models.CharField(default=None, max_length=1000, null=True, blank=True)
    enable = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL,
                                   blank=True, null=True)
    update_by = models.ForeignKey('User', on_delete=models.SET_NULL,
                                   blank=True, null=True)

class Section(models.Model):
    '''
    Model for Section. It is a place in which holding a page.
    '''
    id = models.AutoField(unique=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    placeholder = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL,
                                   blank=True, null=True)
    updated_by = models.ForeignKey('User', on_delete=models.SET_NULL,
                                   blank=True, null=True)


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
    id = models.AutoField(primary_key=True)
    gp_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    form = models.ManyToManyField('Form', through='Group_Form')
    permissions = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey('User', on_delete=models.SET_NULL,
                                   null=True, blank=True)

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
    id = models.IntegerField()
    form_data = models.ForeignKey('Form_Field', on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey('Answer', on_delete=models.SET_NULL, null=True)
    history_info = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Submission(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    page = models.ForeignKey('Page_Form', on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    id = models.BigAutoField(primary_key=True)
    submission = models.ForeignKey('Submission', on_delete=models.CASCADE)
    field = models.ForeignKey('Field', on_delete=models.CASCADE)
    value = models.CharField(default=None, max_length=200)






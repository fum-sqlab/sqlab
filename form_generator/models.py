from django.db import models

# Create your models here.

class Form(models.Model):
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
    pass
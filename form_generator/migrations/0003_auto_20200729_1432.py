# Generated by Django 3.0.3 on 2020-07-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_generator', '0002_auto_20200729_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='forms',
            field=models.ManyToManyField(related_name='forms', through='form_generator.PageForm', to='form_generator.Form'),
        ),
        migrations.AddField(
            model_name='page',
            name='sections',
            field=models.ManyToManyField(related_name='sections', through='form_generator.PageForm', to='form_generator.Section'),
        ),
        migrations.AlterField(
            model_name='group',
            name='form',
            field=models.ManyToManyField(related_name='form', through='form_generator.GroupForm', to='form_generator.Form'),
        ),
    ]
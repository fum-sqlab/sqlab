# Generated by Django 3.0.3 on 2020-08-03 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_generator', '0007_auto_20200802_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='section',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='section',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='section',
            name='updated_on',
        ),
    ]

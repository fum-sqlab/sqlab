# Generated by Django 3.0.3 on 2020-08-25 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_generator', '0016_auto_20200810_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formfield',
            options={'ordering': ['form_id']},
        ),
    ]
# Generated by Django 3.0.3 on 2020-09-02 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_generator', '0018_auto_20200902_1256'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chioce',
            unique_together={('group_name', 'name')},
        ),
    ]

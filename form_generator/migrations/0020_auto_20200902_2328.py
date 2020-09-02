# Generated by Django 3.0.3 on 2020-09-02 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_generator', '0019_auto_20200902_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='field_choices',
        ),
        migrations.AddField(
            model_name='chioce',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='form_generator.FormField'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='chioce',
            unique_together=set(),
        ),
        migrations.DeleteModel(
            name='ChoiceField',
        ),
        migrations.RemoveField(
            model_name='chioce',
            name='group_name',
        ),
    ]
# Generated by Django 3.0.3 on 2020-08-08 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_generator', '0010_answer_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chioce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_generator.Chioce')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_generator.Field')),
            ],
            options={
                'unique_together': {('choice', 'field')},
            },
        ),
        migrations.AddField(
            model_name='field',
            name='field_choices',
            field=models.ManyToManyField(related_name='field_choices', through='form_generator.ChoiceField', to='form_generator.Chioce'),
        ),
    ]
# Generated by Django 3.0.3 on 2020-09-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_generator', '0017_auto_20200825_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='chioce',
            name='group_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chioce',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='chioce',
            unique_together={('group_name',)},
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.RemoveField(
            model_name='chioce',
            name='slug',
        ),
    ]
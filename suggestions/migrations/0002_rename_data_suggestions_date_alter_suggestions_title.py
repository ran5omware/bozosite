# Generated by Django 5.0.1 on 2024-02-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestions',
            old_name='data',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='suggestions',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]

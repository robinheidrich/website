# Generated by Django 3.2.20 on 2023-08-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0002_alter_translation_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
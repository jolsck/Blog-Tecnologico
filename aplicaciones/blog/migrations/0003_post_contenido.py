# Generated by Django 2.2.1 on 2021-07-16 17:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210716_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(default=True, verbose_name='Contenido'),
        ),
    ]
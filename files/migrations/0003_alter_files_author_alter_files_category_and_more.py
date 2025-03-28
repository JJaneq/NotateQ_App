# Generated by Django 5.1.7 on 2025-03-27 02:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_category_remove_files_pdf_files_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='files',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.category'),
        ),
        migrations.AlterField(
            model_name='files',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to='store/files/'),
        ),
        migrations.AlterField(
            model_name='files',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='files',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

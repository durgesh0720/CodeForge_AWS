# Generated by Django 5.1.5 on 2025-01-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeEditor', '0003_file_current_output_file_extainson'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 5.2 on 2025-06-05 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ciudad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='foto',
            field=models.FileField(upload_to='inform'),
        ),
    ]

# Generated by Django 5.2 on 2025-06-05 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ciudad', '0004_alter_ciudad_folleto_alter_ciudad_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='folleto',
            field=models.FileField(blank=True, null=True, upload_to='docu'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='docu'),
        ),
    ]

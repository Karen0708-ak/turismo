# Generated by Django 5.2 on 2025-06-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ciudad', '0003_alter_ciudad_folleto_alter_ciudad_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='folleto',
            field=models.FileField(blank=True, null=True, upload_to='cuidades'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='ciudades'),
        ),
    ]

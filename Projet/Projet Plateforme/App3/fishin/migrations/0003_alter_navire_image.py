# Generated by Django 5.1 on 2025-01-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishin', '0002_navire_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navire',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='navire/'),
        ),
    ]

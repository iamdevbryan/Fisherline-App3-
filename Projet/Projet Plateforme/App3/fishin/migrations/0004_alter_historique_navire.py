# Generated by Django 5.1.6 on 2025-02-27 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishin', '0003_alter_navire_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historique',
            name='navire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fishin.navire'),
        ),
    ]

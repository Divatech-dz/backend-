# Generated by Django 5.1.2 on 2024-10-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]

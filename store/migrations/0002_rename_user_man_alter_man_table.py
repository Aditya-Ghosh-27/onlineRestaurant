# Generated by Django 5.0.7 on 2024-08-08 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='man',
        ),
        migrations.AlterModelTable(
            name='man',
            table='man',
        ),
    ]

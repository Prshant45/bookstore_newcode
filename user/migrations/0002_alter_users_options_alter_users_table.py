# Generated by Django 5.1.7 on 2025-03-29 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['username'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]

# Generated by Django 5.0 on 2024-02-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admineapp', '0012_alter_register_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=8),
        ),
    ]
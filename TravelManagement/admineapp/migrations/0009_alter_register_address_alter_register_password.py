# Generated by Django 5.0 on 2024-02-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admineapp', '0008_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=12),
        ),
    ]
# Generated by Django 5.1.1 on 2024-09-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productentry',
            name='price',
            field=models.IntegerField(),
        ),
    ]
# Generated by Django 4.0.5 on 2022-07-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='dough',
            field=models.CharField(max_length=30),
        ),
    ]

# Generated by Django 3.2.12 on 2022-03-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='size',
        ),
        migrations.AlterField(
            model_name='history',
            name='history',
            field=models.TextField(),
        ),
    ]
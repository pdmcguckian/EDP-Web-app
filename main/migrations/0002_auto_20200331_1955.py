# Generated by Django 3.0.4 on 2020-03-31 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='structuredprojectcode',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='structuredprojectcode',
            name='step',
            field=models.IntegerField(default=1),
        ),
    ]

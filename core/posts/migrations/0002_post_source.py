# Generated by Django 5.1.1 on 2024-09-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

# Generated by Django 3.1.4 on 2021-07-21 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogcomment_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='timestamp',
        ),
    ]
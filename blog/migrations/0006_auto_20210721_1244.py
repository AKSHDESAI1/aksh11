# Generated by Django 3.1.4 on 2021-07-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210721_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 2.2.7 on 2020-02-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsetup', '0005_auto_20200209_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='Options',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2.2 on 2019-07-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20190716_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='registros',
        ),
        migrations.AddField(
            model_name='usuario',
            name='registro',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='token',
            field=models.CharField(default=2, max_length=700),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-16 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190816_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimg',
            name='img',
            field=models.ImageField(upload_to='productImg/'),
        ),
    ]

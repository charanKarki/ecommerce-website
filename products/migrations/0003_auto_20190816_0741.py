# Generated by Django 2.2.3 on 2019-08-16 02:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20190816_0732'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_product',
            new_name='user_ordered_product',
        ),
    ]

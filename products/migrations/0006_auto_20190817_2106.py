# Generated by Django 2.2.3 on 2019-08-17 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190816_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimg',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.ProductDetail'),
        ),
    ]

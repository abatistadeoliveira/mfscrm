# Generated by Django 2.2.6 on 2019-11-18 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_product_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(max_length=5),
        ),
    ]
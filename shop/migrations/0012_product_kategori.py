# Generated by Django 2.2.12 on 2020-12-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kategori',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

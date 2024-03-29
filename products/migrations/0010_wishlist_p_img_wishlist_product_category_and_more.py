# Generated by Django 4.1.4 on 2023-02-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_wishlist_delete_wishproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='p_img',
            field=models.FileField(default=1, upload_to='wishlist/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='product_category',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='product_name',
            field=models.CharField(default=11, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='product_price',
            field=models.CharField(default=111, max_length=255),
            preserve_default=False,
        ),
    ]

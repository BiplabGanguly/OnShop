# Generated by Django 4.1.4 on 2023-02-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='web_admin',
            field=models.CharField(default='false', max_length=500),
        ),
    ]

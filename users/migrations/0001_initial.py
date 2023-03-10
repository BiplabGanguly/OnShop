# Generated by Django 4.1.4 on 2023-02-25 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_admin', models.TextField(default='false', max_length=500)),
                ('address', models.TextField()),
                ('user_pin', models.CharField(blank=True, max_length=255)),
                ('user_dist', models.CharField(blank=True, max_length=255)),
                ('user_state', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2019-10-08 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movierecommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierecommendation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

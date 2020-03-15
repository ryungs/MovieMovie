# Generated by Django 2.2.4 on 2019-10-08 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRecommendation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('KNNRecommendation', models.TextField(default='')),
                ('ALSRecommendation', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 2.2.4 on 2019-09-24 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClusteringState',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('clustering_state', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=500)),
                ('average_rating', models.FloatField(default=0)),
                ('total_rater', models.IntegerField(default=1)),
                ('views_count', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
                ('released', models.TextField(default='')),
                ('runtime', models.TextField(default='')),
                ('director', models.TextField(default='')),
                ('actors', models.TextField(default='')),
                ('country', models.TextField(default='')),
                ('poster', models.TextField(default='')),
                ('ratings', models.TextField(default='')),
                ('male', models.IntegerField(default=0)),
                ('female', models.IntegerField(default=0)),
                ('age10', models.IntegerField(default=0)),
                ('age20', models.IntegerField(default=0)),
                ('age30', models.IntegerField(default=0)),
                ('age40', models.IntegerField(default=0)),
                ('job00', models.IntegerField(default=0)),
                ('job01', models.IntegerField(default=0)),
                ('job02', models.IntegerField(default=0)),
                ('job03', models.IntegerField(default=0)),
                ('job04', models.IntegerField(default=0)),
                ('job05', models.IntegerField(default=0)),
                ('job06', models.IntegerField(default=0)),
                ('job07', models.IntegerField(default=0)),
                ('job08', models.IntegerField(default=0)),
                ('job09', models.IntegerField(default=0)),
                ('job10', models.IntegerField(default=0)),
                ('job11', models.IntegerField(default=0)),
                ('job12', models.IntegerField(default=0)),
                ('job13', models.IntegerField(default=0)),
                ('job14', models.IntegerField(default=0)),
                ('job15', models.IntegerField(default=0)),
                ('job16', models.IntegerField(default=0)),
                ('job17', models.IntegerField(default=0)),
                ('job18', models.IntegerField(default=0)),
                ('job19', models.IntegerField(default=0)),
                ('job20', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserClustering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KMeans_labels', models.IntegerField(default=0)),
                ('HIE_labels', models.IntegerField(default=0)),
                ('GMM_labels', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='M', max_length=10)),
                ('age', models.IntegerField(default=25)),
                ('occupation', models.CharField(max_length=200)),
                ('username', models.CharField(default='DDoromi', max_length=100)),
                ('subscription', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieClustering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GMM_labels', models.IntegerField(default=0)),
                ('HIE_labels', models.IntegerField(default=0)),
                ('KMeans_labels', models.IntegerField(default=0)),
                ('Custom_labels', models.IntegerField(default=0)),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Movie')),
            ],
        ),
    ]

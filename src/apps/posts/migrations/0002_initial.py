# Generated by Django 5.1.4 on 2024-12-13 11:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='housingpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='housing_posts', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='housingpost',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.region', verbose_name='Region'),
        ),
        migrations.AddField(
            model_name='housingpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='posts.housingpostcategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='housingpostimagegallery',
            name='housing_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.housingpost', verbose_name='Housing Post'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_posts', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.region', verbose_name='Region'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.jobpostcategory', verbose_name='Category'),
        ),
    ]

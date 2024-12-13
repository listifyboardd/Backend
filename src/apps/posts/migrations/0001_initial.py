# Generated by Django 5.1.4 on 2024-12-13 11:22

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HousingPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('short_description', models.TextField(max_length=2000, verbose_name='Short description')),
                ('main_image', models.ImageField(upload_to='housing_posts/main_images/', verbose_name='Main image')),
                ('type', models.CharField(choices=[('for_rent', 'For rent'), ('for_business', 'For business')], max_length=255, verbose_name='Type')),
                ('is_draft', models.BooleanField(default=False, verbose_name='Is draft')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HousingPostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HousingPostImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='housing_posts/gallery/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company name')),
                ('salary', models.CharField(max_length=255, verbose_name='Salary')),
                ('type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time')], max_length=10, verbose_name='Type')),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('is_draft', models.BooleanField(default=False, verbose_name='Is draft')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
    ]

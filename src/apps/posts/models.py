from autoslug import AutoSlugField
from django.db import models
from cities_light.models import Region
from src.apps.users.models import CustomUser
from django.utils.text import slugify


class JobPostCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name


class JobPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    company_name = models.CharField(max_length=255, verbose_name='Company name')
    location = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region')
    salary = models.CharField(max_length=255, verbose_name='Salary')
    type = models.CharField(max_length=10, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time')], verbose_name='Type')
    category = models.ForeignKey(JobPostCategory, on_delete=models.CASCADE, verbose_name='Category')
    publication_date = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=False, verbose_name='Is draft')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='job_posts', verbose_name='Author')
    slug = AutoSlugField(populate_from='title', unique=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date']


class HousingPostCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name


class HousingPostImageGallery(models.Model):
    image = models.ImageField(upload_to='housing_posts/gallery/', blank=True, verbose_name='Image')
    housing_post = models.ForeignKey('HousingPost', on_delete=models.CASCADE, verbose_name='Housing Post')

    def __str__(self):
        return f"Image {self.id}"


class HousingPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    short_description = models.TextField(verbose_name='Short description', max_length=2000)
    main_image = models.ImageField(upload_to='housing_posts/main_images/', verbose_name='Main image')
    location = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region')
    type = models.CharField(max_length=255, choices=[('for_rent', 'For rent'), ('for_business', 'For business')], verbose_name='Type')
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(HousingPostCategory, on_delete=models.PROTECT, verbose_name='Category')
    is_draft = models.BooleanField(default=False, verbose_name='Is draft')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='housing_posts', verbose_name='Author')
    slug = AutoSlugField(populate_from='title', unique=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date']
from django.db import models
from cities_light.models import Region

# Create your models here.
class JobPostCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва категорії')

    def __str__(self):
        return self.name

class JobPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Опис')
    publication_date = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регіон')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')
    days_per_week = models.PositiveIntegerField(verbose_name='Кількість днів на тиждень')
    hours_per_day = models.CharField(max_length=20, verbose_name='Години роботи щодня')
    category = models.ForeignKey(JobPostCategory, on_delete=models.CASCADE, verbose_name='Категорія')

    def __str__(self):
        return self.title

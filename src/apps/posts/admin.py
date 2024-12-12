from django.contrib import admin

from src.apps.posts.models import JobPost, JobPostCategory, HousingPost, HousingPostCategory, HousingPostImageGallery

admin.site.register(JobPost)
admin.site.register(JobPostCategory)
admin.site.register(HousingPost)
admin.site.register(HousingPostCategory)
admin.site.register(HousingPostImageGallery)
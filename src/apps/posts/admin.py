from django.contrib import admin

from src.apps.posts.models import JobPost, JobPostCategory

admin.site.register(JobPost)
admin.site.register(JobPostCategory)


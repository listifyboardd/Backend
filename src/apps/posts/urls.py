from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPostViewRead, JobPostCategoryViewRead, HousingPostViewRead, HousingPostCategoryViewRead

router = DefaultRouter()
router.register(r'job-posts', JobPostViewRead, basename='jobpost')
router.register(r'job-post-categories', JobPostCategoryViewRead, basename='jobpostcategory')
router.register(r'housing-posts', HousingPostViewRead, basename='housingpost')
router.register(r'housing-post-categories', HousingPostCategoryViewRead, basename='housingpostcategory')

urlpatterns = [
    path('', include(router.urls)),
]
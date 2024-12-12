from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPostViewRead, JobPostCategoryViewRead, HousingPostViewRead, HousingPostCategoryViewRead, UserJobPostsListView, UserHousingPostsListView, JobPostCreateView, HousingPostCreateView, JobPostUpdateView, HousingPostUpdateView, JobPostDeleteView, HousingPostDeleteView

router = DefaultRouter()
router.register(r'job-posts', JobPostViewRead, basename='jobpost')
router.register(r'job-post-categories', JobPostCategoryViewRead, basename='jobpostcategory')
router.register(r'housing-posts', HousingPostViewRead, basename='housingpost')
router.register(r'housing-post-categories', HousingPostCategoryViewRead, basename='housingpostcategory')

urlpatterns = [
    path('', include(router.urls)),
    path('user/job-posts/', UserJobPostsListView.as_view(), name='user_job_posts'),
    path('user/housing-posts/', UserHousingPostsListView.as_view(), name='user_housing_posts'),

    path('user/job-posts/create/', JobPostCreateView.as_view(), name='job_post_create'),
    path('user/housing-posts/create/', HousingPostCreateView.as_view(), name='housing_post_create'),

    path('user/job-posts/<int:pk>/update/', JobPostUpdateView.as_view(), name='job_post_update'),
    path('user/housing-posts/<int:pk>/update/', HousingPostUpdateView.as_view(), name='housing_post_update'),

    path('user/job-posts/<int:pk>/delete/', JobPostDeleteView.as_view(), name='job_post_delete'),
    path('user/housing-posts/<int:pk>/delete/', HousingPostDeleteView.as_view(), name='housing_post_delete'),
]
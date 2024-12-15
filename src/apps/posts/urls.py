from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobPostViewRead, JobPostCategoryViewRead, HousingPostViewRead, HousingPostCategoryViewRead, UserJobPostsListView, UserHousingPostsListView, JobPostCreateView, HousingPostCreateView, JobPostUpdateView, HousingPostUpdateView, JobPostDeleteView, HousingPostDeleteView, JobPostDetailView, HousingPostDetailView

router = DefaultRouter()
router.register(r'job-posts', JobPostViewRead, basename='jobpost')
router.register(r'job-post-categories', JobPostCategoryViewRead, basename='jobpostcategory')
router.register(r'housing-posts', HousingPostViewRead, basename='housingpost')
router.register(r'housing-post-categories', HousingPostCategoryViewRead, basename='housingpostcategory')

urlpatterns = [
    path('', include(router.urls)),

    path('job-posts/<slug:slug>/', JobPostDetailView.as_view(), name='job_post_detail'),
    path('housing-posts/<slug:slug>/', HousingPostDetailView.as_view(), name='job_post_detail'),

    path('user/job-posts/', UserJobPostsListView.as_view(), name='user_job_posts'),
    path('user/housing-posts/', UserHousingPostsListView.as_view(), name='user_housing_posts'),

    path('user/job-posts/create/', JobPostCreateView.as_view(), name='job_post_create'),
    path('user/housing-posts/create/', HousingPostCreateView.as_view(), name='housing_post_create'),

    path('user/job-posts/<slug:slug>/update/', JobPostUpdateView.as_view(), name='job_post_update_slug'),
    path('user/housing-posts/<slug:slug>/update/', HousingPostUpdateView.as_view(), name='housing_post_update_slug'),

    path('user/job-posts/<slug:slug>/delete/', JobPostDeleteView.as_view(), name='job_post_delete_slug'),
    path('user/housing-posts/<slug:slug>/delete/', HousingPostDeleteView.as_view(), name='housing_post_delete_slug'),

]
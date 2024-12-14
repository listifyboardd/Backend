from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PostTitleSearchView

router = DefaultRouter()
router.register(r'job-posts', views.JobPostViewRead, basename='job_posts')
router.register(r'housing-posts', views.HousingPostViewRead, basename='housing_posts')

urlpatterns = [
    path('', include(router.urls)),
    path('user/job-posts/', views.UserJobPostsListView.as_view(), name='user_job_posts'),
    path('user/housing-posts/', views.UserHousingPostsListView.as_view(), name='user_housing_posts'),
    path('job-posts/category/<slug:slug>/', views.JobPostCategoryFilterView.as_view(), name='job_posts_category_filter'),
    path('job-posts/categories/', views.JobPostCategoryViewList.as_view(), name='job_posts_categories'),
    path('housing-posts/category/<slug:slug>/', views.HousingPostCategoryFilterView.as_view(), name='housing_posts_category_filter'),
    path('housing-posts/categories/', views.HousingPostCategoryViewList.as_view(), name='housing_posts_categories'),

    path('user/job-posts/create/', views.JobPostCreateView.as_view(), name='job_post_create'),
    path('user/housing-posts/create/', views.HousingPostCreateView.as_view(), name='housing_post_create'),

    path('user/job-posts/<int:pk>/update/', views.JobPostUpdateView.as_view(), name='job_post_update'),
    path('user/housing-posts/<int:pk>/update/', views.HousingPostUpdateView.as_view(), name='housing_post_update'),

    path('user/job-posts/<int:pk>/delete/', views.JobPostDeleteView.as_view(), name='job_post_delete'),
    path('user/housing-posts/<int:pk>/delete/', views.HousingPostDeleteView.as_view(), name='housing_post_delete'),
    path('location/countries', views.LocationCountryViewList.as_view(), name='posts_location_countries'),
    path('location/regions', views.LocationRegionViewList.as_view(), name='posts_location_regions'),
    path('location/country-regions/', views.LocationCountryRegionsViewList.as_view(), name='location_country_regions'),
    path('job-posts/location-filter/', views.JobPostLocationFilterView.as_view(), name='job_posts_location_filter'),
    path('housing-posts/location-filter/', views.HousingPostLocationFilterView.as_view(), name='housing_posts_location_filter'),
    path('posts-search/', PostTitleSearchView.as_view(), name='posts-search'),

]

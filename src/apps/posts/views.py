from django.shortcuts import render
from rest_framework import viewsets
from .models import JobPostCategory, JobPost, HousingPostCategory, HousingPost
from .serializers import JobPostCategorySerializer, JobPostSerializer, HousingPostCategorySerializer, \
    HousingPostSerializer


class JobPostViewRead(viewsets.ReadOnlyModelViewSet):
    queryset = JobPost.objects.filter(is_draft=False)
    serializer_class = JobPostSerializer


class JobPostCategoryViewRead(viewsets.ReadOnlyModelViewSet):
    queryset = JobPostCategory.objects.all()
    serializer_class = JobPostCategorySerializer


class HousingPostViewRead(viewsets.ReadOnlyModelViewSet):
    queryset = HousingPost.objects.filter(is_draft=False)
    serializer_class = HousingPostSerializer


class HousingPostCategoryViewRead(viewsets.ReadOnlyModelViewSet):
    queryset = HousingPostCategory.objects.all()
    serializer_class = HousingPostCategorySerializer


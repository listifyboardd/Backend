from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .models import JobPostCategory, JobPost, HousingPostCategory, HousingPost
from .serializers import JobPostCategorySerializer, JobPostSerializer, HousingPostCategorySerializer, HousingPostSerializer


class UserJobPostsListView(generics.ListAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobPost.objects.filter(author=self.request.user)


class UserHousingPostsListView(generics.ListAPIView):
    serializer_class = HousingPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HousingPost.objects.filter(author=self.request.user)


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


class JobPostCreateView(generics.CreateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class HousingPostCreateView(generics.CreateAPIView):
    serializer_class = HousingPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class JobPostUpdateView(generics.UpdateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied("You can only update your own posts.")
        serializer.save()


class HousingPostUpdateView(generics.UpdateAPIView):
    queryset = HousingPost.objects.all()
    serializer_class = HousingPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied("You can only update your own posts.")
        serializer.save()


class JobPostDeleteView(generics.DestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You can only delete your own posts.")
        instance.delete()


class HousingPostDeleteView(generics.DestroyAPIView):
    queryset = HousingPost.objects.all()
    serializer_class = HousingPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You can only delete your own posts.")
        instance.delete()
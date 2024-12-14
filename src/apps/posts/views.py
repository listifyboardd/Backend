from cities_light.models import Country, Region
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .models import JobPostCategory, JobPost, HousingPostCategory, HousingPost
from .serializers import (
    JobPostCategorySerializer,
    JobPostSerializer,
    HousingPostCategorySerializer,
    HousingPostSerializer,
    LocationCountrySerializer,
    LocationRegionSerializer, PostSerializer
)


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
    lookup_field = 'slug'
    queryset = JobPost.objects.filter(is_draft=False)
    serializer_class = JobPostSerializer


class JobPostCategoryViewList(generics.ListAPIView):
    queryset = JobPostCategory.objects.all()
    serializer_class = JobPostCategorySerializer


class HousingPostViewRead(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'slug'
    queryset = HousingPost.objects.filter(is_draft=False)
    serializer_class = HousingPostSerializer


class HousingPostCategoryViewList(generics.ListAPIView):
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


class JobPostCategoryFilterView(generics.ListAPIView):
    serializer_class = JobPostSerializer

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        return JobPost.objects.filter(category__slug=category_slug, is_draft=False)


class HousingPostCategoryFilterView(generics.ListAPIView):
    serializer_class = HousingPostSerializer

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        return HousingPost.objects.filter(category__slug=category_slug, is_draft=False)


class LocationCountryViewList(generics.ListAPIView):
    serializer_class = LocationCountrySerializer
    queryset = Country.objects.all()


class LocationRegionViewList(generics.ListAPIView):
    serializer_class = LocationRegionSerializer
    queryset = Region.objects.all()


class LocationCountryRegionsViewList(generics.ListAPIView):
    serializer_class = LocationRegionSerializer
    http_method_names = ['post']

    def get_queryset(self):
        country_id = self.request.data.get('country_id')
        return Region.objects.filter(country_id=country_id)


class JobPostLocationFilterView(generics.ListAPIView):
    serializer_class = JobPostSerializer
    http_method_names = ['post']

    def get_queryset(self):
        country_id = self.request.data.get('country_id', '')
        region_id = self.request.data.get('region_id', '')
        if country_id and region_id:
            return JobPost.objects.filter(location__region__country_id=country_id, location__region_id=region_id,
                                          is_draft=False)
        elif country_id:
            return JobPost.objects.filter(location__region__country_id=country_id, is_draft=False)
        elif region_id:
            return JobPost.objects.filter(location__region_id=region_id, is_draft=False)

        return JobPost.objects.filter(is_draft=False)


class HousingPostLocationFilterView(generics.ListAPIView):
    serializer_class = HousingPostSerializer
    http_method_names = ['post']

    def get_queryset(self):
        country_id = self.request.data.get('country_id', '')
        region_id = self.request.data.get('region_id', '')
        if country_id and region_id:
            return HousingPost.objects.filter(location__region__country_id=country_id, location__region_id=region_id,
                                              is_draft=False)
        elif country_id:
            return HousingPost.objects.filter(location__region__country_id=country_id, is_draft=False)
        elif region_id:
            return HousingPost.objects.filter(location__region_id=region_id, is_draft=False)
        return HousingPost.objects.filter(is_draft=False)


class PostTitleSearchView(generics.ListAPIView):
    def get_serializer_class(self):
        return PostSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', '')
        job_posts = JobPost.objects.filter(title__icontains=title, is_draft=False)
        housing_posts = HousingPost.objects.filter(title__icontains=title, is_draft=False)
        return list(job_posts) + list(housing_posts)

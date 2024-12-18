from cities_light.models import Country, Region
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response

from .models import JobPostCategory, JobPost, HousingPostCategory, HousingPost
from .permissions import IsOwner
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
    queryset = JobPost.objects.filter(is_draft=False)
    serializer_class = JobPostSerializer
    lookup_field = 'slug'


class JobPostCategoryViewRead(viewsets.ReadOnlyModelViewSet):
    queryset = JobPostCategory.objects.all()
    serializer_class = JobPostCategorySerializer
    pagination_class = None


class HousingPostViewRead(viewsets.ReadOnlyModelViewSet):
    queryset = HousingPost.objects.filter(is_draft=False)
    serializer_class = HousingPostSerializer
    lookup_field = 'slug'


class HousingPostCategoryViewRead(viewsets.ReadOnlyModelViewSet):
    queryset = HousingPostCategory.objects.all()
    serializer_class = HousingPostCategorySerializer
    pagination_class = None


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
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'slug'


class HousingPostUpdateView(generics.UpdateAPIView):
    queryset = HousingPost.objects.all()
    serializer_class = HousingPostSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'slug'


class JobPostDeleteView(generics.DestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'slug'


class HousingPostDeleteView(generics.DestroyAPIView):
    queryset = HousingPost.objects.all()
    serializer_class = HousingPostSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'slug'


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
    pagination_class = None


class LocationRegionViewList(generics.ListAPIView):
    serializer_class = LocationRegionSerializer
    queryset = Region.objects.all()
    pagination_class = None


class LocationCountryRegionsViewList(generics.ListAPIView):
    serializer_class = LocationRegionSerializer
    http_method_names = ['post']
    pagination_class = None

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        country_id = self.request.data.get('country_id')
        return Region.objects.filter(country_id=country_id)


class JobPostLocationFilterView(generics.GenericAPIView):
    serializer_class = JobPostSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        country_id = self.request.data.get('country_id', '')
        region_id = self.request.data.get('region_id', '')
        queryset = JobPost.objects.filter(is_draft=False)

        if country_id and region_id:
            queryset = queryset.filter(location__country_id=country_id, location_id=region_id)
        elif country_id:
            queryset = queryset.filter(location__country_id=country_id)
        elif region_id:
            queryset = queryset.filter(location_id=region_id)
        return queryset


class HousingPostLocationFilterView(generics.GenericAPIView):
    serializer_class = HousingPostSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        country_id = self.request.data.get('country_id', '')
        region_id = self.request.data.get('region_id', '')
        queryset = HousingPost.objects.filter(is_draft=False)

        if country_id and region_id:
            queryset = queryset.filter(location__country_id=country_id, location_id=region_id)
        elif country_id:
            queryset = queryset.filter(location__country_id=country_id)
        elif region_id:
            queryset = queryset.filter(location_id=region_id)
        return queryset


class PostTitleSearchView(generics.ListAPIView):
    def get_serializer_class(self):
        return PostSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', '')
        job_posts = JobPost.objects.filter(title__icontains=title, is_draft=False)
        housing_posts = HousingPost.objects.filter(title__icontains=title, is_draft=False)
        return list(job_posts) + list(housing_posts)
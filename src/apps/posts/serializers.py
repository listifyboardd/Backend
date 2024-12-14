from cities_light.models import Country, Region
from rest_framework import serializers
from .models import JobPost, JobPostCategory, HousingPostCategory, HousingPostImageGallery, HousingPost


class JobPostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True, required=False)
    location_name = serializers.CharField(source='location.display_name', read_only=True, required=False)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = JobPost
        fields = '__all__'


class JobPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostCategory
        fields = '__all__'


class HousingPostImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingPostImageGallery
        fields = '__all__'


class HousingPostSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(use_url=True)
    gallery = HousingPostImageGallerySerializer(many=True, source='housingpostimagegallery_set', read_only=True,
                                                required=False)
    category_name = serializers.CharField(source='category.name', read_only=True, required=False)
    location_name = serializers.CharField(source='location.display_name', read_only=True, required=False)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = HousingPost
        fields = '__all__'


class HousingPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingPostCategory
        fields = '__all__'


class LocationCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class LocationRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')


class PostSerializer(serializers.Serializer):
    type = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    def get_type(self, obj):
        if isinstance(obj, JobPost):
            return 'job'
        elif isinstance(obj, HousingPost):
            return 'housing'
        return 'unknown'

    def get_data(self, obj):
        if isinstance(obj, JobPost):
            return JobPostSerializer(obj).data
        elif isinstance(obj, HousingPost):
            return HousingPostSerializer(obj).data
        return {}

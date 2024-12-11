from rest_framework import serializers
from .models import JobPost, JobPostCategory, HousingPostCategory, Images, HousingPost


class JobPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostCategory
        fields = '__all__'

class JobPostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=JobPostCategory.objects.all())
    class Meta:
        model = JobPost
        fields = '__all__'

class HousingPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingPostCategory
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class HousingPostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=HousingPostCategory.objects.all())
    main_image = serializers.ImageField(use_url=True)
    other_images = ImagesSerializer(many=True, read_only=True)
    class Meta:
        model = HousingPost
        fields = '__all__'
from rest_framework import serializers
from apps.uploader.models import OriginalImage
from rest_framework import serializers


class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginalImage
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    portfolio_image = serializers.ImageField(source='portfolio_image.portfolio_field')
    landscape_image = serializers.ImageField(source="landscape_image.landscape_field")
    logo_image = serializers.ImageField(source='logo_image.logo_field')
    

    class Meta:
        model = OriginalImage
        fields = ['title', 'image', 'portfolio_image', 'landscape_image','logo_image' ]
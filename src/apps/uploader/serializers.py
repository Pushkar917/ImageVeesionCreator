from rest_framework.serializers import ModelSerializer
from apps.uploader.models import OriginalImage


class ImageCreateSerializer(ModelSerializer):
    class Meta:
        model = OriginalImage
        fields = '__all__'
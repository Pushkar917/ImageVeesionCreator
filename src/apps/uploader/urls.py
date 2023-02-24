from django.urls import path
from apps.uploader.views import ImageBasedAPIView

urlpatterns = [
    path('uploadImage', ImageBasedAPIView.as_view(), name="imageUpload")
]
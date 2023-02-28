from django.urls import path
from apps.uploader.views import ImageBasedAPIView, request_image, UserBasedImageView

urlpatterns = [
    path('uploadImage', ImageBasedAPIView.as_view(), name="imageUpload"),
    path('', request_image, name="home"),
    path('<str:title>', UserBasedImageView.as_view(), name="home")
]
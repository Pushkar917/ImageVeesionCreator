from django.urls import path, re_path
from apps.uploader.views import ImageBasedAPIView, single_image_page,request_image, UserBasedImageView

urlpatterns = [
    path('', request_image, name="postimage"),
    path('<str:title>', single_image_page, name="single_image_page"),
    path('uploadImage', ImageBasedAPIView.as_view(), name="imageUpload"),
]
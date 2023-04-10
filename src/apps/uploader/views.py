from django.shortcuts import redirect, render  
from apps.uploader.forms import ImageUploadForms
from apps.uploader.models import OriginalImage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.uploader.serializers import ImageCreateSerializer, ImageSerializer

def request_image(request):
    if request.method == "POST":
        form = ImageUploadForms(request.POST, request.FILES)
        if form.is_valid():
            image_object = form.instance
            image_data=OriginalImage.objects.create(title=image_object.title, image= image_object.image)
            image_data.save()
            processed_images = OriginalImage.objects.get(pk=image_data.pk) 
            return render(request,"success.html", context={"processed_images": processed_images})

    else:  
        form = ImageUploadForms()  
  
    return render(request, 'imageForm.html', {'form': form})






def single_image_page(request, title):
    processed_images = OriginalImage.objects.get(title=title)
    if processed_images: 
        return render(request,"success.html", context={"processed_images": processed_images})



class UserBasedImageView(APIView):
    def get(self, request, title):
        # authorization code
        processed_images = OriginalImage.objects.get(title=title) 
        return render(request,"success.html", context={"processed_images": processed_images})


class ImageBasedAPIView(APIView):
    def post(self, request):
        data = request.data
        imgSerializerClass = ImageCreateSerializer(data=data)
        if imgSerializerClass.is_valid():
            imgSerializerClass.save()
            return Response(imgSerializerClass.data, status=status.HTTP_201_CREATED)
        else:
            return Response(imgSerializerClass.error, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        images = OriginalImage.objects.all()
        serializer_class = ImageSerializer(images, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
   


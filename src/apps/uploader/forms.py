from django import forms
from apps.uploader.models import OriginalImage


class ImageUploadForms(forms.ModelForm):
    class Meta:
        model = OriginalImage
        fields = '__all__'
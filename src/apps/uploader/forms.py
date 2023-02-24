from django import forms


class ImageUploadForms(forms.ModelForm):
    class Meta:
        fields = '__all__'
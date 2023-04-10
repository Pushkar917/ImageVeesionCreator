from django.urls import path
from apps.users.views import UserAPIView

urlpatterns = [
    path('createuser', UserAPIView.as_view(), name="createuser"),
    
]
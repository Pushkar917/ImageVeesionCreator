from django.urls import path

from apps.core.views import register, home, logout_request

urlpatterns = [
     path('', home, name='home'),
     path('register', register, name='register'),
     path('logout', logout_request, name='logout'),
]
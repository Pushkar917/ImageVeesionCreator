from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    contact_list = serializers.JSONField()

    class Meta:
        model = User
        fields = '__all__'
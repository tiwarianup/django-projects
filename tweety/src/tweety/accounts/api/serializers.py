from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse_lazy

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    followerCount = serializers.SerializerMethodField()
    profileUrl = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'followerCount',
            'profileUrl'
        ]

    def get_followerCount(self, obj):
        return 0
    
    def get_profileUrl(self, obj):
        return reverse_lazy('profiles:details', kwargs={"username": obj.username})
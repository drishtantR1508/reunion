from rest_framework import serializers
from .models import UserProfileInfo

class UserProfileInfoSerializer(serializers.ModelSerializer):
    # username = serializers
    id = serializers.IntegerField()
    followers = serializers.CharField(source='count_followers')
    following = serializers.CharField(source='count_following')
    username = serializers.CharField(source='__str__')

    class Meta:
        model = UserProfileInfo
        fields = ['id','username','email','contact','followers','following']
from django.shortcuts import render
from .serializers import UserProfileInfoSerializer
from .models import UserProfileInfo
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user_profile = UserProfileInfo.objects.get(id = request.user.id)
        serializer = UserProfileInfoSerializer(user_profile)
        return Response(serializer.data)        

class FollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,pk,format=None):
        profile = get_object_or_404(UserProfileInfo,id=pk)
        response = Response()
        if not profile.followers.filter(id=request.user.id).exists():
            profile.followers.add(request.user)
            profile = UserProfileInfo.objects.get(user=request.user)
            user = User.objects.get(id=pk)
            print(user)
            profile.following.add(user)
            response.data = {
                'message': 'Successfully followed',
            }
        else:
            response.data = {
                'message': 'Already Followed',
            }

        return response
        
class UnfollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,pk,format=None):
        profile = get_object_or_404(UserProfileInfo,id=pk)
        response = Response()
        if profile.followers.filter(id=request.user.id).exists():
            profile.followers.remove(request.user)
            profile = UserProfileInfo.objects.get(user=request.user)
            user = User.objects.get(id=pk)
            print(user)
            profile.following.remove(user)
            response.data = {
                'message': 'Successfully unfollowed',
            }
        else:
            response.data = {
                'message': 'Already Unfollowed',
            }

        return response
 
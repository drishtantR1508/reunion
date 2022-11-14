from django.urls import path,include
from .views import UserProfileAPIView,FollowAPIView,UnfollowAPIView

urlpatterns = [
    path('',UserProfileAPIView.as_view()),
    path('follow/<int:pk>',FollowAPIView.as_view()),
    path('unfollow/<int:pk>',UnfollowAPIView.as_view()),
]

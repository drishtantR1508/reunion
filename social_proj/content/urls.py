from django.urls import path,include
from .views import PostAPIView,CommentAPIView,PostLikeAPIView,PostUnlikeAPIView

urlpatterns = [
    path('posts/',PostAPIView.as_view()),
    path('all_posts/',PostAPIView.as_view()),
    path('posts/<int:pk>',PostAPIView.as_view()),
    path('comment/<int:pk>',CommentAPIView.as_view()),
    path('like/<int:pk>',PostLikeAPIView.as_view()),
    path('unlike/<int:pk>',PostUnlikeAPIView.as_view()),
    path('user/',include('user.urls'))
]
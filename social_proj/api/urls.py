from django.urls import path,include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authenticate/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #post and comment related urls will bebhandled by content app urls
    path('',include('content.urls')),
    path('user/',include('user.urls')),

]
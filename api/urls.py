from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter


from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('group', GroupViewSet)
router.register('follow', FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('redoc/', TemplateView.as_view(template_name='redoc2.html'), name='redoc2'),
]



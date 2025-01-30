from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (CommentViewSet, GroupViewSet, PostViewSet,
                       FollowCreateAPIView)


v1_router_api = DefaultRouter()
v1_router_api.register('posts', PostViewSet)
v1_router_api.register('groups', GroupViewSet)
v1_router_api.register('follow', FollowCreateAPIView, basename='follow')
v1_router_api.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(v1_router_api.urls)),
    path('v1/', include('djoser.urls.jwt')),
]

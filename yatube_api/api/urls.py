from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (CommentViewSet, GroupViewSet, PostViewSet,
                       FollowViewSet)


v1_router_api = DefaultRouter()
v1_router_api.register('posts', PostViewSet)
v1_router_api.register('groups', GroupViewSet)
# v1_router_api.register('follow', FollowViewSet, basename='follow')
v1_router_api.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(v1_router_api.urls)),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/follow/', FollowViewSet.as_view()),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views


router_v1 = DefaultRouter()
router_v1.register('posts',
                   views.PostViewSet,
                   basename='posts')
router_v1.register('groups',
                   views.GroupReadOnlyViewSet,
                   basename='groups')
router_v1.register('follow',
                   views.FollowViewSet,
                   basename='follow')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   views.CommentViewSet,
                   basename='comments')


urlpatterns_v1 = [
    path('', include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),
]

urlpatterns = [
    path('v1/', include(urlpatterns_v1)),
]

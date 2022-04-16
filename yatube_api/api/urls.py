from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import PostsViewSet, GroupsViewSet, CommentsViewSet
from rest_framework.authtoken import views

router_v1 = SimpleRouter()
router_v1.register('v1/posts', PostsViewSet, basename='api/v1/posts')
router_v1.register('v1/groups', GroupsViewSet, basename='api/v1/groups')
router_v1.register(r'v1/posts/(?P<post_id>[^/.]+)/comments',
                   CommentsViewSet, basename='api/v1/comments')
# router.register('comments', GroupsViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

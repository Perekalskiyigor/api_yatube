from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import PostsViewSet, GroupsViewSet, CommentsViewSet
from rest_framework.authtoken import views

router = SimpleRouter()
router.register('api/v1/posts', PostsViewSet, basename='api/v1/posts')
router.register('api/v1/groups', GroupsViewSet, basename='api/v1/groups')
router.register(r'api/v1/posts/(?P<post_id>[^/.]+)/comments',
                CommentsViewSet, basename='api/v1/comments')
# router.register('comments', GroupsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/posts/', ..., name='api/v1/posts-list'),
    # path('api/v1/posts/<int:pk>/', ..., name='api/v1/posts-detail'),
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token)
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    # path('api-token-auth/', views.obtain_auth_token),
    # path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    # path('auth/', include('djoser.urls.jwt')),


]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

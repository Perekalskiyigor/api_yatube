# from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import PostsViewSet, GroupsViewSet
GroupsViewSet

router = SimpleRouter()
router.register('posts', PostsViewSet)
router.register('groups', GroupsViewSet)


urlpatterns = [
    # DefaultRouter, то в ответ на GET-запрос к адресу
    # http://127.0.0.1:8000/ вернётся список ссылок на доступные ресурсы
    # path('', ..., name='api-root'),
    # Посты
    # path('api/v1/posts/', ..., name='posts-list'),
    # path('api/v1/posts/<int:pk>/', ..., name='posts-detail'),
    # Группы
    # path('api/v1/groups/', ..., name='groups-list'),
    # path('api/v1/groups/<int:pk>/', ..., name='groups-detail'),

]

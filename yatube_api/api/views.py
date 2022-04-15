# views.py
# from django.shortcuts import get_object_or_404, render
# from requests import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from posts.models import Group, Post, Comment
from .serializers import PostsSerializer, GroupSerializer, CommentsSerializer
from rest_framework.views import PermissionDenied
# Create your views here.


# Получаем все посты
class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого поста невозможно!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого поста невозможно!')
        instance.delete()


# Получаем все группы
class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Получаем все комменты к одному посту
class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        # Получаем id поста из эндпоинта
        post_id = self.kwargs.get("post_id")
        # И отбираем только нужные комментарии
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Измнение чужого комментария не возможно")
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("Удаление чужого комментария не возможно")
        return super().perform_destroy(instance)

    # def retrieve(self, request, *args, **kwargs):
        # if request.author != self.request.user:
        # raise PermissionDenied ("Изменение чужого комментария не возможно")
        # return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import serializers
from posts.models import Group, Post, Comment


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class PostsSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')

from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post


User = get_user_model()


class BaseSerializer(serializers.ModelSerializer):
    """Базовый сериализатор."""

    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        fields = '__all__'


class PostSerializer(BaseSerializer):
    """Сериализатор для работы с публикациями."""

    class Meta(BaseSerializer.Meta):
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с группами."""

    class Meta(BaseSerializer.Meta):
        model = Group


class CommentSerializer(BaseSerializer):
    """Сериализатор для работы с комментариями."""

    class Meta(BaseSerializer.Meta):
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с подписками."""
    user = serializers.SlugRelatedField(read_only=True,
                                        slug_field='username')
    following = serializers.SlugRelatedField(queryset=User.objects.all(),
                                             slug_field='username')

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        user = self.context['request'].user
        if value == user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        if Follow.objects.filter(user=user, following=value).exists():
            raise serializers.ValidationError(
                f"Вы уже подписаны на {value.username}!"
            )
        return value

from rest_framework import serializers
from api.models import Snippet, Comment, User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'snippets')
        write_only_fields = ('password', )


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    score = serializers.Field(source='score')

    class Meta:
        model = Comment
        exclude = ('parent', 'snippet')
        read_only_fields = ('edited', )


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')  # Field is readonly
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Snippet
        read_only_fields = ('highlighted', )
from rest_framework import serializers
from reviewer.models import Snippet, Comment, User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'snippets')
        write_only_fields = ('password', )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.RelatedField()
    parent = serializers.RelatedField()
    score = serializers.Field(source='score')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'body', 'created', 'parent', 'score')
        write_only_fields = ('snippet', 'edited', )


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username') # Field is readonly
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'display_linenos', 'language', 'style', 'owner', 'comments')
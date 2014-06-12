from rest_framework import serializers
from reviewer.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):

    owner = serializers.Field(source='owner.username') # Field is readonly

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'snippets')
        write_only_fields = ('password', )


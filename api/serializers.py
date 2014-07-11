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

    def validate_line_references(self, attrs, source):
        """
        Check that all line references are valid and compress adjacent references
        """
        reference_list = attrs[source]

        if not isinstance(reference_list, list):
            raise serializers.ValidationError("Reference list should be a list.")

        # So far this is the only way I can think of accessing the relevant snippet
        print self.context['request'].parser_context['kwargs']['pk']

        return attrs

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
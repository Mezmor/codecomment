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

        compressed_list = []
        reference_list = sorted(list(set(reference_list)))

        # So far this is the only way I can think of accessing the relevant snippet
        snippet = Snippet.objects.get(id=self.context['request'].parser_context['kwargs']['pk'])

        for line_ref in reference_list:
            if line_ref > snippet.linenos or line_ref <= 0:
                raise serializers.ValidationError("Can't reference a non-existent line.")

        for line in reference_list:
            if not compressed_list:  # First line reference
                compressed_list.append(line)
            else:
                if isinstance(compressed_list[-1], tuple):
                    (under, prev_line) = compressed_list[-1]
                    if line == (prev_line + 1):
                        compressed_list[-1] = (under, line)
                    else:
                        compressed_list.append(line)
                else:
                    if line == (compressed_list[-1] + 1):
                        compressed_list[-1] = (compressed_list[-1], line)
                    else:
                        compressed_list.append(line)

        print compressed_list

        attrs[source] = compressed_list

        return attrs

    class Meta:
        model = Comment
        exclude = ('parent', 'snippet')
        read_only_fields = ('edited', )


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')  # Field is readonly
    comments = CommentSerializer(many=True, read_only=True)


    def validate_code(self, attrs, source):
        code = attrs[source]

        if code.isspace():
            raise serializers.ValidationError("Can not be only whitespace.")

        return attrs

    class Meta:
        model = Snippet
        read_only_fields = ('highlighted', 'linenos', )
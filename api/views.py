from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.permissions import IsOwnerOrReadOnly
from api.models import Snippet, User, Comment
from api.serializers import SnippetSerializer, UserSerializer, CommentSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list-create', request=request, format=format),
        'snippets': reverse('snippet-list-create', request=request, format=format)
    })

"""
Snippet views
"""


class SnippetListCreate(generics.ListCreateAPIView):
    """
    GET:
        - All snippets
    POST:
        - Create a snippet
    Permissions:
        - User must be authenticated to POST
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET:
        - A snippet
    PUT:
        - Update a snippet
    PATCH:
        - Update a snippet
    DELETE:
        - Delete a snippet
    Permissions:
        - User must be authenticated and the snippet owner to edit
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetHighlight(generics.GenericAPIView):
    """
    GET:
        - Highlighted code snippet
    """
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class CommentCreation(generics.CreateAPIView):
    """
    POST to create a comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.owner = self.request.user
        obj.snippet = Snippet.objects.get(id=int(self.kwargs['pk']))


class CommentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'comment_pk'

    def pre_save(self, obj):
        obj.edited = True

"""
User views
"""


class UserListCreate(generics.ListCreateAPIView):
    """
    GET:
        - All users
    POST:
        - Create a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post_save(self, obj, created=False):
        """
        On creation, replace the raw password with a hashed version
        """
        if created:
            obj.set_password(obj.password)
            obj.save()


class UserDetail(generics.RetrieveAPIView):
    """
    Get:
        - A user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

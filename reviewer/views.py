from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from reviewer.permissions import IsOwnerOrReadOnly
from reviewer.models import Snippet
from reviewer.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

"""
Snippet views
"""

class SnippetCreate(generics.CreateAPIView):
    """
    Create a snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetList(generics.ListAPIView):
    """
    List all snippets
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a given snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.owner = self.request.user

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)



"""
User views
"""

class UserList(generics.ListAPIView):
    """
    List all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
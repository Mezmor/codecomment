from django.conf.urls import patterns, url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('api.views',
    url(r'^$', 'api_root'),

    url(r'^snippets/$', views.SnippetListCreate.as_view(), name='snippet-list-create'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^snippets/(?P<pk>[0-9]+)/comments/$', views.CommentCreation.as_view(), name='comment-create'),
    url(r'^snippets/(?P<pk>[0-9]+)/comments/(?P<comment_pk>[0-9]+)/$', views.CommentUpdate.as_view(), name='comment-update'),

    url(r'^users/$', views.UserListCreate.as_view(), name='user-list-create'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
)

urlpatterns = format_suffix_patterns(urlpatterns)
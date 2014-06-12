from django.conf.urls import patterns, url
from reviewer import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('reviewer.views',
    url(r'^$', 'api_root'),

    url(r'^snippets/$', views.SnippetListCreate.as_view(), name='snippet-list-create'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),

    url(r'^users/$', views.UserListCreate.as_view(), name='user-list-create'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
)

urlpatterns = format_suffix_patterns(urlpatterns)
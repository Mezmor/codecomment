from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail')
)

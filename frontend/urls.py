from django.conf.urls import patterns, include, url
urlpatterns = patterns('frontend.views',
    url(r'^$', 'home',name='home')
    )

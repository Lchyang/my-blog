from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post, name='post'),
]
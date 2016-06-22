from django.conf.urls import patterns, include, url
from .views import addlike,addcomment,post_list,post_detail,post_new,chat,about,PostHabr
urlpatterns = [
        url(r'^$', post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
        url(r'^post/new/$', post_new, name='post_new'),
        url(r'^addlike/(?P<com_id>\d+)/$',addlike),
        url(r'^addcomment/$',addcomment),
        url(r'^chat/$',chat),
        url(r'^about/$',about),
        url(r'^h/$', PostHabr, name='PostHabr'),
    ]
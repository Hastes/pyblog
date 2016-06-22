from django.conf.urls import patterns, include, url
from .views import login, logout
urlpatterns = [
        url(r'login/', login, name='loginapp.views.login'),
        url(r'logout/', logout, name='loginapp.views.logout'),
    ]

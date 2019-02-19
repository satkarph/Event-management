"""satkar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from event.views import get_index, EventListView, EventDetailView, EventCreateView ,EventDeleteView, EventUpdateView
from accounts.views import login
from accounts.views import register
from accounts.views import logout
from accounts.views import profile

app_name = "event"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index),
    url(r'^accounts/login$', login, name = 'login'),
    url(r'^accounts/register$', register, name = 'register'),
    url(r'^accounts/logout$', logout, name = 'logout'),
    url(r'^accounts/profile$', profile, name = 'profile'),
    url(r'^list/$',EventListView.as_view(),name='list'),
    url(r'^list/(?P<pk>\d+)/$',EventDetailView.as_view(),name='detail'),
    url(r'^create/$',EventCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',EventUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',EventDeleteView.as_view(),name='delete')

    ]
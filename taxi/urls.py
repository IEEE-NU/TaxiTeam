from django.conf.urls import patterns, include, url
from django.contrib import admin
from taxi import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taxi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^matchtime/', views.matchtime),
    url(r'^groupinfo/', views.groupinfo),
)

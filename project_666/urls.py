from django.conf.urls import  url, patterns,include
import sys
from django.contrib import admin


urlpatterns = patterns(
    'blog',
url(r'^$', 'views.home', name='home'),
url(r'^admin/', include(admin.site.urls)),

)



"""
#from blog import views
#url(r'^$', 'views.home', name='home')


project_666 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

#from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',

    url(r'', include('hello.urls')),
    url(r'^blog/', include(blog_urls)),
)

"""

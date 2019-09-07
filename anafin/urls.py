"""anafin URL Configuration

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
from django.urls import  path,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from anaform import views
from django.contrib.auth.decorators import login_required
from dummypage import views as dummyviews
# from anafin import anaform
# admin.autodiscover()
# MEDIA_ROOT = '/images/'    
# MEDIA_URL = '/localhost:8000/images/'  
urlpatterns = [
	path('protodashboard/', include('dashboard.urls')),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/',views.home,name='home'),
    url(r'^main/',views.mainpage,name='main'),
    url(r'^dummy/',dummyviews.dummypage,name='dummy'),
    url(r'^runlogic/',dummyviews.runlogic,name='runlogic'),
    url(r'^dummysuccess/',dummyviews.dummysuccess,name='dummysuccess'),
    url(r'^dummyrt/',dummyviews.dummyrt,name='dummyrt'),


    # url(r'^$', login_required(BoardView.as_view()), name='boards'),
    
    # url(r'^login/$', auth_views.LoginView.as_view(
    #     template_name='login.html'), name='login'),
    # url(r'^logout/$', auth_views.LogoutView.as_view(
    #     template_name='login.html'), name='logout'),

]

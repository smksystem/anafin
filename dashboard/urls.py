from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    url(r'^$', views.index, name='index'),
]	
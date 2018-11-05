from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [

    url(r'^$', views.clientDirection, name='clientDirection'),

    # ^$ - means Don't add anything with the url
    # clientDirection is a function in views.py


    url(r'^singleMarker/$',  views.singleMarker,  name='singleMarker'),
    url(r'^stylishMap/$',    views.stylishMap,    name='stylishMap'),

]


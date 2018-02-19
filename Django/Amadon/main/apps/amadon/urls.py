from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^amadon/$', views.index),
    url(r'^/buy/$', views.buy),
    url(r'^checkout/$', views.cart)
]

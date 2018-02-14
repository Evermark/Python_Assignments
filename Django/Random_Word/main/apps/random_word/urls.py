from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^random_word/$', views.index),
    url(r'^random_word/generate/$', views.random_word, name = 'generate'),
    url(r'^random_word/reset/$', views.reset, name = 'reset')
  ]

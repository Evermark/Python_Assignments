from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^session_words/$', views.index),
    url(r'^session/add_words$', views.add_words),
    url(r'^session_words/clear$', views.clear)
]

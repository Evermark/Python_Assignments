from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.index), #displays all users
    url(r'^users/new$', views.new), #displays form to add user
    url(r'^users/(?P<user_id>\d+)$', views.show_or_update), #updates user info
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit), #display editng from user
    url(r'^users/(?P<user_id>\d+)/destroy$', views.destroy),
]

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index), #routing to index method
    url(r'^new$', views.new), #routing to new method
    url(r'^(?P<number>\d+)$', views.show), #routing to show method
    url(r'^(?P<number>\d+)/edit$', views.edit), #routing to edit method
    url(r'^(?P<number>\d+)/delete$', views.destroy), #routing to destroy method
    url(r'^$', views.create)
]
 #methods located in views.py

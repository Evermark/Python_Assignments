from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ninja_gold$', views.index),
    url(r'^process_money$', views.process_money),
]

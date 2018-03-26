from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^books$', views.books), #displays all book reviews
    url(r'^books/add$', views.add), #displays page to add new book review
    url(r'^books/(?P<book_id>\d+)$', views.register), #shows all reviews for book
    url(r'^books/users/(?P<user_id>\d+)$', views.register) #shows user info
    ]

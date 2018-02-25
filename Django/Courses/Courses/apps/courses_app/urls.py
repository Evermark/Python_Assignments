from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^courses$', views.index), #display all courses
    url(r'^courses/create$', views.create),#create new course
    url(r'^courses/(?P<course_id>\d+)/delete$', views.delete), #display all courses
    url(r'^courses/(?P<course_id>\d+)$', views.show), #display course to be deleted

]

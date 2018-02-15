from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^survey_form/$', views.survey),
    url(r'^survey_form/process$', views.process),
    url(r'^survey_form/result$', views.result)
]

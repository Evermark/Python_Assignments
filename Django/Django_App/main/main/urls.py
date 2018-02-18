"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

/ - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.

/new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.

/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /.

/{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.

/{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.

/{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /.
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.blogs_app.urls')),
    url(r'^blogs_app/', include('apps.blogs_app.urls')),
    url(r'^', include('apps.session_words.urls'))
]

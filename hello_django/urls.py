"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
"""
from django.conf.urls import url
from django.contrib import admin
from notes.views import NoteList, NoteAdd, NoteEdit, NoteDelete

urlpatterns = [
	url(r'^$', NoteList.as_view(), name='note_list'),
    url(r'^add/', NoteAdd.as_view(), name='note_add'),  
    url(r'^(?P<id>\d+)/edit/$', NoteEdit.as_view(), name='note_edit'),  
	url(r'^(?P<id>\d+)/delete/$', NoteDelete.as_view(), name='note_delete'),	
    url(r'^admin/', admin.site.urls),
]

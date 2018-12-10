from django.conf.urls import url
from . import views
from blog import views

#url for pages
urlpatterns = [
	url(r'^contact$', views.contact, name='contact.html'),
	url(r'^events$', views.events, name='events.html'),
	url(r'^$', views.index, name='index.html'),
	url(r'^post1$', views.post1, name='post1.html'),
	url(r'^post2$', views.post2, name='post2.html'),
	url(r'^post3$', views.post3, name='Post3.html'),
]
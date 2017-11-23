from django.conf.urls import include, url
from apple import views

urlpatterns = [
	url(r'^$', views.home, name='homepage')
]
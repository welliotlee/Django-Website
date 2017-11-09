from django.conf.urls import include, url
from newp_app1 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	]
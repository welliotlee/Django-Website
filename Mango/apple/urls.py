from django.conf.urls import include, url
from apple import views

urlpatterns = [
	url(r'^$', views.home, name='homepage'),
	url(r'^faq/', views.faq, name='faq'),
	url(r'^guide/(?P<guide_name_slug>[\w\-]+)/$', views.guide, name='guide'),
	url(r'^add_guide/$', views.add_guide, name='add_guide'),
	url(r'^list_guides/$', views.list_guides, name='list_guides'),
	url(r'^rate_guides/$', views.rate_guides, name='rate_guides'),
]
from django.conf.urls import url
from . import views

app_name = 'finclusion'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$',views.register, name='register'),
	url(r'^registration/$', views.registration, name='registration'),
	url(r'^sms/$', views.smsRes)
]

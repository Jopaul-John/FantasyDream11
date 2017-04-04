from django.conf.urls import url
from . import  views


app_name='fantasyapp'
urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^adminlogin/$', views.adminlogin),
    url(r'^cricket/$', views.cricket),
    url(r'^cricket/(?P<id>[0-9]+)/$', views.cricket_matches),
    url(r'^football/$', views.football),
    url(r'^football/(?P<id>[0-9]+)/$', views.football_match),
    url(r'^crictournament/(?P<id>[0-9]+)/$',views.crictournament),
    url(r'^foottournament/(?P<id>[0-9]+)/$', views.foottournament),
    url(r'^logout/$', views.logout_view),
    url(r'^post/$', views.post),

]
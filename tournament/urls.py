from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^profile/', views.edit_profile, name='profile'),
    url(r'^players/$', views.players, name='players'),
    url(r'^about/$', views.about, name='about'),
    url(r'^create/$', views.create_tournament, name='create'),
    url(r'^delete/(?P<tournament_id>[0-9]+)/$', views.delete_tournament, name='delete'),
    url(r'^(?P<tournament_name>[\w]+)/$', views.tournament, name='tournament'),
    url(r'^(?P<tournament_name>[\w]+)/(?P<stage_id>[0-9]+)/$', views.table, name='table')
]

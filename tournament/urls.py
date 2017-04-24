from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.TournamentList.as_view(), name='main'),
    url(r'^create/$', views.create_tournament, name='create_tourn'),
    url(r'^profile/', views.edit_profile, name='profile'),
    url(r'^players/$', views.PlayersList.as_view(), name='players'),
    url(r'^about/$', views.about, name='about'),
    url(r'^generate/tourn(?P<tourn_id>[0-9]+)/$', views.create_teams, name='create_teams'),
    url(r'^delete/tourn(?P<tourn_id>[0-9]+)/$', views.delete_tournament, name='delete_tourn'),
    url(r'^tourn(?P<tourn_id>[0-9]+)/$', views.StageList.as_view(), name='tournament'),
    url(r'^tourn(?P<tourn_id>[0-9]+)/stage(?P<stage_id>[0-9]+)/table/$', views.TableList.as_view(), name='table'),
    url(r'^tourn(?P<tourn_id>[0-9]+)/stage(?P<stage_id>[0-9]+)/matches/$', views.MatchesList.as_view(), name='matches'),
    url(r'^tourn(?P<tourn_id>[0-9]+)/stage(?P<stage_id>[0-9]+)/matches/match_score/$', views.match_score, name='score'),
    url(r'^tourn(?P<tourn_id>[0-9]+)/stage(?P<stage_id>[0-9]+)/create_matches/$', views.create_matches, name='create_matches'),
]
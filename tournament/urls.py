from django.conf.urls import url
from . import views


'''urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^profile/', views.edit_profile, name='profile'),
    url(r'^players/$', views.players, name='players'),
    url(r'^about/$', views.about, name='about'),
    url(r'^create/$', views.create_tournament, name='create'),
    url(r'^delete/(?P<tournament_id>[0-9]+)/$', views.delete_tournament, name='delete'),
    url(r'^generate/(?P<tournament_id>[0-9]+)/$', views.create_teams, name='generate'),
    url(r'^(?P<tournament_name>[\w\s]+)/$', views.tournament, name='tournament'),
    url(r'^(?P<tournament_name>[\w\s]+)/(?P<stage_id>[0-9]+)/$', views.table, name='table'),
    url(r'^(?P<tournament_name>[\w\s]+)/matches/(?P<stage_id>[0-9]+)/$', views.create_matches, name='matches'),
    url(r'^(?P<tournament_name>[\w\s]+)/(?P<stage_id>[0-9]+)/match-list/$', views.show_matches, name='show'),
    url(r'^(?P<tournament_name>[\w\s]+)/(?P<stage_id>[0-9]+)/match-list/match_score/$', views.match_score, name='score'),
]'''


urlpatterns = [
    url(r'^$', views.TournamentList.as_view(), name='main'),
    url(r'^tourn(?P<tourn_id>[0-9]+)/$', views.StageList.as_view(), name='tournament'),
    url(r'^tourn(?P<tourn_id>[0-9]+)/stage(?P<stage_id>)[0-9]+/$', views.TableList.as_view(), name='table'),
    url(r'^tourn(?P<tourn_id>[0-9]+)/stage(?P<stage_id>)[0-9]+/matches/$', views.MatchesList.as_view(), name='matches'),
]
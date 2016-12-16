from django.contrib import admin
from .models import Player, Tournament, Team, Round, Match, Stage


admin.site.register((Player, Tournament, Team, Round, Match, Stage))


class PlayerAdmin(admin.ModelAdmin):
    pass

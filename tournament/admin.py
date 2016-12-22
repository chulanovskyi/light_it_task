from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Player, Tournament, Team, Round, Match, Stage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _


admin.site.register((Player, Tournament, Team, Round, Match, Stage))


class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)
        self.fields['first_name'] = forms.CharField(label=_('First name'), max_length=50)
        self.fields['last_name'] = forms.CharField(label=_('Last name'), max_length=50)

UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')
    }),
)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

from django.contrib import admin

from .models import Actor, Film

admin.site.register([Actor, Film])

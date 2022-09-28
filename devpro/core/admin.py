from django.contrib import admin

from .models import Actor, Film, FilmActor, Category, FilmCategory


class ActorInline(admin.TabularInline):
    model = FilmActor


class CategoryInline(admin.TabularInline):
    model = FilmCategory


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'length', 'release_year')
    inlines = (ActorInline, CategoryInline)


admin.site.register([Actor, Category])

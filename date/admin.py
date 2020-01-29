from django.contrib import admin

from date.models import Onl, Event, Birth, Death


class EventInLine(admin.TabularInline):
    model = Event, Death, Birth


@admin.register(Onl)
class OnlAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ('month', 'date',)
    search_fields = ("month", 'date',)
    prepopulated_fields = {'slug': ('month', 'date',)}


from django.contrib import admin

from .models import Bus, Stop


class BusAdmin(admin.ModelAdmin):
    list_display = ("bus_number", "direction", "stop", "lat", "long")


class StopAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "lat", "long")


admin.site.register(Bus, BusAdmin)
admin.site.register(Stop, StopAdmin)

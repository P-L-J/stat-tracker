from django.contrib import admin
from tracker.models import Activity, Stat


class ActivityAdmin(admin.ModelAdmin):
    # list_display = ['user', 'url', 'short', 'timestamp', 'title',
    #                 'description']
    pass

admin.site.register(Activity, ActivityAdmin)

class StatAdmin(admin.ModelAdmin):
    # list_display = ['user', 'url', 'short', 'timestamp', 'title',
    #                 'description']
    pass

admin.site.register(Stat, ActivityAdmin)

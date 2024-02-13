from django.contrib import admin

from svetofors.models import Svetofor


class SvetoforsInline(admin.TabularInline):
    model = Svetofor

admin.site.register(Svetofor)
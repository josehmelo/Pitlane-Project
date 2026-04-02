from django.contrib import admin
from .models import Time

class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'atividade')
    search_fields = ('nome',)

admin.site.register(Time, TimeAdmin)

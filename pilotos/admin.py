from django.contrib import admin
from .models import Piloto, Piloto_Status

class PilotoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'codigo', 'equipe')
    list_filter = ('equipe', 'nacionalidade')

class PilotoStatusAdmin(admin.ModelAdmin):
    list_display = ('piloto', 'temporada', 'pontos', 'posicao')

admin.site.register(Piloto, PilotoAdmin)
admin.site.register(Piloto_Status, PilotoStatusAdmin)

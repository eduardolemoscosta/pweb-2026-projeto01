from django.contrib import admin
from .models import Homepage, Jogador, Sobre


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ('titulo',)


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'posicao', 'idade', 'nascimento')
    search_fields = ('nome', 'posicao')


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('site_nome', 'autor')

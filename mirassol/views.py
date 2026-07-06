from django.shortcuts import render

from .models import Homepage, Jogador, Sobre


def inicio(request):
    homepage = Homepage.objects.first()
    if homepage:
        context = {
            'titulo': homepage.titulo,
            'historico': homepage.historico,
            'estadio_url': homepage.estadio_url,
        }
    else:
        context = {
            'titulo': 'Mirassol Futebol Clube',
            'historico': 'Fundado em 1925, o Mirassol FC é um clube do interior paulista que se destacou nas últimas décadas com acessos nacionais e campanhas fortes no Campeonato Paulista. O clube é conhecido como o Leão Caipira e joga no Estádio Maião, em Mirassol.',
            'estadio_url': 'https://upload.wikimedia.org/wikipedia/commons/7/76/Est%C3%A1dio_Jos%C3%A9_Maria_de_Campos_Maia_-_Mirassol.jpg',
        }
    return render(request, 'inicio.html', context)


def equipe(request):
    jogadores = Jogador.objects.all()
    return render(request, 'equipe.html', {'jogadores': jogadores})


def sobre(request):
    sobre_obj = Sobre.objects.first()
    if sobre_obj:
        context = {
            'site_nome': sobre_obj.site_nome,
            'autor': sobre_obj.autor,
            'descricao': sobre_obj.descricao,
        }
    else:
        context = {
            'site_nome': 'Portal Mirassol FC',
            'autor': 'Eduardo e João Pedro',
            'descricao': 'Projeto acadêmico em Django que apresenta informações sobre o Mirassol Futebol Clube usando templates herdeiros e dados passados por contexto.',
        }
    return render(request, 'sobre.html', context)

from django.db import migrations


def create_jogadores(apps, schema_editor):
    Jogador = apps.get_model('mirassol', 'Jogador')
    jogadores = [
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/Georgemy.png?v=1773345563',
            'nome': 'Georgemy',
            'idade': 30,
            'posicao': 'Goleiro',
            'nascimento': 'Americana, SP',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/daniel-borges_2fc38be8-b5c3-47c5-815c-022e31fe7eb6.png?v=1773150618',
            'nome': 'Daniel Borges',
            'idade': 32,
            'posicao': 'Lateral-direito',
            'nascimento': 'São José dos Campos, SP',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/wilian-machado.png?v=1773150618',
            'nome': 'Willian Machado',
            'idade': 29,
            'posicao': 'Zagueiro',
            'nascimento': 'Meleiro, SC',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/rodrigues_253b2adb-4104-48e4-821c-d40d382a8052.png?v=1773150618',
            'nome': 'Rodrigues',
            'idade': 28,
            'posicao': 'Zagueiro',
            'nascimento': 'Arês, RN',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/eduardo_482585d8-fe8f-4e1b-82f8-88532f4c451d.png?v=1773150618',
            'nome': 'Eduardo',
            'idade': 36,
            'posicao': 'Meio-campista',
            'nascimento': 'Ribeirão Preto, SP',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/lucas-mugni_b85b241c-0731-47c4-9b04-7979d8f8da54.png?v=1773150618',
            'nome': 'Lucas Mugni',
            'idade': 34,
            'posicao': 'Meio-campista',
            'nascimento': 'Santa Fé, Argentina',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/neto-moura_dd5edc9e-0ba3-4536-8d23-5d2c3402d1b4.png?v=1773150618',
            'nome': 'Neto Moura',
            'idade': 29,
            'posicao': 'Meio-campista',
            'nascimento': 'Atalaia, AL',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/Vini-bacchi.png?v=1773345563',
            'nome': 'Vinicius Bacchi',
            'idade': 18,
            'posicao': 'Atacante',
            'nascimento': 'Brasil',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/Tiquinho-Soares.png?v=1773325970',
            'nome': 'Tiquinho Soares',
            'idade': 35,
            'posicao': 'Atacante',
            'nascimento': 'Sousa, PB',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/nathan-fogaca_2d7f0cb6-07f4-4539-8cba-3c8b44f9b0d8.png?v=1773150618',
            'nome': 'Nathan Fogaça',
            'idade': 26,
            'posicao': 'Atacante',
            'nascimento': 'Palmeira, PR',
        },
        {
            'foto': 'https://www.mirassolfc.com.br/cdn/shop/files/Georgemy.png?v=1773345563',
            'nome': 'Galeano',
            'idade': 27,
            'posicao': 'Atacante',
            'nascimento': 'Brasil',
        },
    ]

    for jogador_data in jogadores:
        Jogador.objects.get_or_create(
            nome=jogador_data['nome'],
            defaults=jogador_data,
        )


def remove_jogadores(apps, schema_editor):
    Jogador = apps.get_model('mirassol', 'Jogador')
    nomes = [
        'Georgemy',
        'Daniel Borges',
        'Willian Machado',
        'Rodrigues',
        'Eduardo',
        'Lucas Mugni',
        'Neto Moura',
        'Vinicius Bacchi',
        'Tiquinho Soares',
        'Nathan Fogaça',
        'Galeano',
    ]
    Jogador.objects.filter(nome__in=nomes).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('mirassol', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_jogadores, remove_jogadores),
    ]

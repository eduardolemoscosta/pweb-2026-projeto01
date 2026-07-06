from django.db import models


class Homepage(models.Model):
    titulo = models.CharField('Título', max_length=120)
    historico = models.TextField('Histórico')
    estadio_url = models.URLField('URL do Estádio', blank=True)

    class Meta:
        verbose_name = 'Página Inicial'
        verbose_name_plural = 'Páginas Iniciais'

    def __str__(self):
        return self.titulo


class Jogador(models.Model):
    foto = models.URLField('Foto')
    nome = models.CharField('Nome', max_length=120)
    idade = models.PositiveIntegerField('Idade')
    posicao = models.CharField('Posição', max_length=80)
    nascimento = models.CharField('Naturalidade', max_length=120)

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

    def __str__(self):
        return self.nome


class Sobre(models.Model):
    site_nome = models.CharField('Nome do Site', max_length=160)
    autor = models.CharField('Autor', max_length=120)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return self.site_nome

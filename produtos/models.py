from django.db import models

# Create your models here.


class Produtos(models.Model):
    disponibilidade_choices = (
        ('S', 'SIM'),
        ('N', 'NAO'),
    )
    nome = models.CharField(max_length=200, verbose_name='Nome do produto')
    descricao = models.CharField(max_length=200, verbose_name='Descrição do produto')
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor do produto')
    quantidade = models.BigIntegerField(verbose_name='quantidade de produtos')
    disponivel = models.CharField(max_length=1, choices=disponibilidade_choices, verbose_name='Disponibilidade')

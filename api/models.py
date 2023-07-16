from django.db import models
from django.core.validators import MinValueValidator

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
       return self.nome

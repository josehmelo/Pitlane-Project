from django.db import models

# Create your models here.

class Time(models.Model):
    nome = models.CharField(max_length=100)
    nome_completo = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    construtor_id = models.CharField(max_length=100, unique=True)
    campeonatos = models.IntegerField(default=0)
    entrada = models.IntegerField(null=True, blank=True)
    atividade = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['nome']
        
    def __str__(self):
        return self.nome
    
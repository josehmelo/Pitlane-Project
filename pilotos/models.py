from django.db import models
from times.models import Time

# Create your models here.

class Piloto(models.Model):
    apelido = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    piloto_id = models.CharField(max_length=100, unique=True)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    aniversario = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=50)
    numero = models.IntegerField(null=True, blank=True)
    atividade = models.BooleanField(default=True)
    equipe = models.ForeignKey(Time, on_delete=models.SET_NULL, null=True, blank=True, related_name='pilotos')
    
    
    class Meta:
        ordering = ['nome']
        
    def __str__(self):
        return f"{self.nome} ({self.apelido})"
    
class Piloto_Status(models.Model):
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE, related_name='status')
    temporada = models.IntegerField()
    posicao = models.IntegerField(null=True, blank=True)
    pontos = models.IntegerField(default=0)
    vitorias = models.IntegerField(default=0)
    podiums = models.IntegerField(default=0)
    poles  = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-temporada']
        unique_together = ('piloto', 'temporada')
        
    def __str__(self):
        return f"{self.piloto} - {self.temporada}"
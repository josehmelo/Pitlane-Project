from rest_framework import serializers
from .models import Piloto, Piloto_Status
from times.serializers import TimeSerializer

class PilotoStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto_Status
        fields = '__all__'
        
class PilotoSerializer(serializers.ModelSerializer):
    time_details = TimeSerializer(source='time', read_only=True)
    nome_completo =  serializers.SerializerMethodField()
    
    class Meta:
        model = Piloto
        fields = '__all__'
    def get_nome_completo(self, obj):
        return f"{obj.nome} {obj.sobrenome}"
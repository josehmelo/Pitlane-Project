from rest_framework import serializers
from .models import Time

class TimeSerializer(serializers.ModelSerializer):
    pilotos_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Time
        fields = '__all__'
        
    def get_pilotos_count(self, obj):
        return obj.pilotos.count()
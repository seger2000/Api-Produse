from rest_framework import serializers
from .models import Produse

class ProduseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produse
        fields = '__all__'
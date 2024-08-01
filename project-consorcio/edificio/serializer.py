from rest_framework import serializers
from .models import Edificio

class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        fields = "__all__"
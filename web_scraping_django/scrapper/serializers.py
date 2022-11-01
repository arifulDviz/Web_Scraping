from .models import Bilbasen_data, Biltorvet_data
from rest_framework import serializers


class Bilbasen_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bilbasen_data
        fields = '__all__'


class Biltorvet_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biltorvet_data
        fields = '__all__'

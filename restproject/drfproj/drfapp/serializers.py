from rest_framework import serializers
from .models import Studant

class StudantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studant
        fields= (
            'name','age'
        )
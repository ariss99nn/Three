from rest_framework import serializers
from .models import Input

class Input_Serializer(serializers.Serializer):
    class Meta:
        model = Input
        fields = '__all__'


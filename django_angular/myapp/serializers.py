from rest_framework import serializers
from . import models

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Register
        fields = ('petition', 'email', 'date', 'quantity')
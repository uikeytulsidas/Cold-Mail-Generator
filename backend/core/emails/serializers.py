from rest_framework import serializers
from .models import Lead, GeneratedEmail

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class GeneratedEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedEmail
        fields = '__all__'


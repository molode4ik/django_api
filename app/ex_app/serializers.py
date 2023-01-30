from rest_framework import serializers
from .models import Teaser


class TeaserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teaser
        fields = '__all__'

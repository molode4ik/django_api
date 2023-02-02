from rest_framework import serializers
from .models import Teaser, Author


class TeaserSerializer(serializers.ModelSerializer):
    author_id = serializers.RelatedField(source='Author', read_only=True)

    class Meta:
        model = Teaser
        fields = '__all__'


class WorkTeasersSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Teaser.objects.all())

    class Meta:
        model = Teaser
        fields = ('id', 'status', )



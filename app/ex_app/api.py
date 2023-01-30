from rest_framework import viewsets, permissions
from .models import Teaser
from .serializers import TeaserSerializer


class TeaserViewSet(viewsets.ModelViewSet):
    queryset = Teaser.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeaserSerializer




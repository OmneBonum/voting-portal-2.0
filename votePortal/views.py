from rest_framework import viewsets
from votePortal import serializers
from . import models as voteModels

class DistrictsView(viewsets.ModelViewSet):
    queryset = voteModels.Districts.objects.all()
    serializer_class = serializers.DistrictsSerializer
    # permission_classes = (permissions.AllowAny,)


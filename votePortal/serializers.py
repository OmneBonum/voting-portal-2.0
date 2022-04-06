from rest_framework import serializers
from . import models as voteModels

class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = voteModels.Districts
        fields = "__all__"

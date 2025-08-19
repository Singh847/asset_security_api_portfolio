from rest_framework import serializers
from .models import CloudAsset

class CloudAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudAsset
        fields = '__all__'

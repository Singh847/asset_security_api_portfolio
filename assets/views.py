# assets/views.py

from rest_framework import viewsets, permissions
from django.http import JsonResponse
from django.core.mail import send_mail

from .models import CloudAsset
from .serializers import CloudAssetSerializer


class CloudAssetViewSet(viewsets.ModelViewSet):
    queryset = CloudAsset.objects.all()
    serializer_class = CloudAssetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        asset = serializer.save()
        send_mail(
            subject='New Asset Added',
            message=f"Asset '{asset.name}' of type '{asset.asset_type}' was added.",
            from_email='noreply@yourapp.com',
            recipient_list=['admin@yourapp.com'],
        )


# Home route for root URL (/)
def home_view(request):
    return JsonResponse({"message": "Welcome to the Asset Security API"})
import boto3
from botocore.exceptions import BotoCoreError, ClientError

def simulate_ec2_creation(name, region):
    print(f"Simulating EC2 instance creation: {name} in {region}")
    # In real use, you'd call boto3 EC2 APIs here
    return True

def simulate_s3_creation(name, region):
    print(f"Simulating S3 bucket creation: {name} in {region}")
    # In real use, you'd call boto3 S3 APIs here
    return True


class CloudAssetViewSet(viewsets.ModelViewSet):
    queryset = CloudAsset.objects.all()
    serializer_class = CloudAssetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        asset = serializer.save()

        if asset.asset_type.upper() == "EC2":
            success = simulate_ec2_creation(asset.name, asset.region)
        elif asset.asset_type.upper() == "S3":
            success = simulate_s3_creation(asset.name, asset.region)
        else:
            success = False

        # Send email/log only if successful
        if success:
            send_mail(
                subject='AWS Asset Added',
                message=f"Asset '{asset.name}' of type '{asset.asset_type}' was added in region '{asset.region}'.",
                from_email='noreply@yourapp.com',
                recipient_list=['admin@yourapp.com'],
            )

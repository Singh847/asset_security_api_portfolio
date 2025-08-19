from django.db import models

class CloudAsset(models.Model):
    ASSET_TYPES = [('EC2', 'EC2 Instance'), ('S3', 'S3 Bucket')]
    name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPES)
    region = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset_type} - {self.name}"

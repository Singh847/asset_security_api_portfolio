from rest_framework import generics
from assets.userserializers.serializers import UserSerializer


from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework.generics import CreateAPIView

from .models import User
from . import serializers

# Create your views here.


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterUserSerializer

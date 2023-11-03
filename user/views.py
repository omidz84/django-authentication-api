from django.utils.translation import gettext as _

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import User
from . import serializers

# Create your views here.


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterUserSerializer


class LoginUserView(GenericAPIView):
    serializer_class = serializers.LoginUserSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)


class LogoutUserView(GenericAPIView):
    serializer_class = serializers.LogoutUserSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': _('logout OK.')}, status.HTTP_200_OK)


class RefreshTokenView(GenericAPIView):
    serializer_class = serializers.RefreshTokenSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)


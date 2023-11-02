from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import User
from .utils import get_tokens


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8, label=_('confirm password'), write_only=True, required=True)
    token = serializers.SerializerMethodField(read_only=True, label=_('token'))

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'code_melli',
            'email',
            'address',
            'location',
            'password',
            'password2',
            'token'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_token(self, obj):
        user = User.objects.get(phone_number=obj.phone_number)
        token = get_tokens(user)
        refresh = token['refresh']
        access = token['access']
        return {'access': access, 'refresh': refresh}

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise ValidationError(_('The passwords must match'))
        return data

    def create(self, validated_data):
        data = validated_data
        user = User.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number'],
            code_melli=data['code_melli'],
            address=data['address'],
            location=data['location'],
            password=data['password']
        )
        return user


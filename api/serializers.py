from rest_framework import serializers
from api.models import Device, User, Data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('created_at',)


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        # fields = '__all__'
        exclude = ('created_at',)


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
        # exclude = ('created_at',)

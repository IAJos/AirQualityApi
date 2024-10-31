from django.shortcuts import render
from rest_framework import generics
from api.models import User, Data, Device
from api.serializers import UserSerializer, DataSerializer, DeviceSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        device = self.request.query_params.get('device', None)
        if device is not None:
            queryset = queryset.filter(device=device)
        return queryset


class DeviceList(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        permission_classes = [IsAuthenticated]
        queryset = Device.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset


class DataList(generics.ListCreateAPIView):
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        permission_classes = [IsAuthenticated]
        queryset = Data.objects.all().order_by('-created_at')
        data = self.request.query_params.get('data', None)
        if data is not None:
            queryset = queryset.filter(data=data)
        return queryset


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()

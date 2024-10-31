from django.urls import path
from api.views import DeviceList, DeviceDetail, DataList, DataDetail, UserList, UserDetail

urlpatterns = [
    path('devices/', DeviceList.as_view()),
    path('devices/<int:pk>/', DeviceDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('data/', DataList.as_view()),
    path('data/<int:pk>/', DataDetail.as_view())
]
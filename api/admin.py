from django.contrib import admin
from api.models import User, Device, Data

import airQuality

# Register your models here.

admin.site.register(Device)
admin.site.register(Data)
admin.site.register(User)

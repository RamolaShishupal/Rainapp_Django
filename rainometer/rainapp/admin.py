from django.contrib import admin


# Register your models here
from . models import volenteer
from .models import raindata

admin.site.register(volenteer)
admin.site.register(raindata)


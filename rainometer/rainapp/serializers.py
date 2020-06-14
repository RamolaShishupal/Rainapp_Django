from rest_framework import serializers
from . models import volenteer
from  .models import raindata

class volenteerSerializer(serializers.ModelSerializer):
    class Meta:
        model=volenteer
        fields=('name','email')

class raindataSerializer(serializers.ModelSerializer):
    class Meta:
        model=raindata
        fields=('rain','enterytime')

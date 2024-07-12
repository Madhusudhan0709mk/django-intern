from rest_framework import serializers

from .models import *

class DataentrySerializers(serializers.ModelSerializer):
    class Meta:
        model=DataEntry
        fields='__all__'
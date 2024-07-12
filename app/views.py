
from rest_framework import generics
from .models import *
from .serializers import *


class DataView(generics.ListAPIView):
    queryset= DataEntry.objects.all()
    serializer_class=DataentrySerializers
from rest_framework import viewsets
from . import models
from . import serialize

class apiViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serialize.ProductSerializer  
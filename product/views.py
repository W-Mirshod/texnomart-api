from rest_framework import generics
from rest_framework.permissions import AllowAny

from product.models import Product
from product.serializers import ProductSerializer


class Products(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Release, Patch, Product, Image
from .serializers import ReleaseSerializer, PatchSerializer, ProductSerializer, ImageSerializer
from .permissions import IsAdmin, IsProductManager, IsProductOwner

class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [IsAdmin]  # Only admins can manage releases

class PatchViewSet(viewsets.ModelViewSet):
    queryset = Patch.objects.all()
    serializer_class = PatchSerializer
    permission_classes = [IsAdmin | IsProductManager]  # Admin and Product Managers can manage patches

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin | IsProductManager | IsProductOwner]  # Different roles for product management

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdmin | IsProductOwner]  # Only admins and product owners can manage images

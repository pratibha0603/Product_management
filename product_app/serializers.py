from rest_framework import serializers
from .models import Release, Patch, Product, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class PatchSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Patch
        fields = '__all__'

class ReleaseSerializer(serializers.ModelSerializer):
    patches = PatchSerializer(many=True, read_only=True)

    class Meta:
        model = Release
        fields = '__all__'

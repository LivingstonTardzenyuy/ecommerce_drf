from rest_framework import Serializer
from products.models import  Atrribute, Brand, Product, Category, ProductLine, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(seriallizers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerializer(seriailizers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
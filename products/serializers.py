from rest_framework import serializers
from products.models import (
    Attribute,
    Brand,
    Product,
    Category,
    ProductLine,
    ProductImage,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()   #Due to the foriegn key we have
    category = CategorySerializer()   #Due to the foriegn key we have
    
    class Meta:
        model = Product
        fields = "__all__"

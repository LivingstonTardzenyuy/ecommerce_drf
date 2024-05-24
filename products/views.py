from django.shortcuts import render
from products.serializers import *
from products.models import *
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from drf_spectacular.utils import extend_schema


# Create your views here.
class CategoryView(viewsets.ViewSet):
    """_summary_
    Simple ViewSets for Viewing the Categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serailizer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandView(viewsets.ViewSet):
    """_summary_
    Simple Viewsets for viewing all Brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

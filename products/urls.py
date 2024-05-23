from django.urls import path
from rest_framework.routers import DefaultRouter
from .models import CategoryView


router = DefaultRouter()
router.register("category", CategoryView, basename="category")

urlpatterns = [router.urls]

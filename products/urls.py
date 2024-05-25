from django.urls import path, include
from .views import CategoryView, BrandView, ProductView
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"", CategoryView)
router.register(r"brand", BrandView)
router.register(r"product", ProductView)

urlpatterns = [path("", include(router.urls))]

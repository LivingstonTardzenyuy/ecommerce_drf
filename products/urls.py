from django.urls import path, include
from .views import CategoryView, BrandView
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"", CategoryView)
router.register(r"brand", BrandView)

urlpatterns = [path("", include(router.urls))]

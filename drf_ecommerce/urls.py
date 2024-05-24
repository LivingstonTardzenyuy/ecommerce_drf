from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="swagger-ui",
    ),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="swagger-ui")),
]

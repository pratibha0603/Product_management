from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReleaseViewSet, PatchViewSet, ProductViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'releases', ReleaseViewSet)
router.register(r'patches', PatchViewSet)
router.register(r'products', ProductViewSet)
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

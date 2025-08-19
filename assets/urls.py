from django.urls import path
from .views import CloudAssetViewSet, home_view  # <-- Add this
from assets.RegisterView.views import RegisterView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'assets', CloudAssetViewSet)

urlpatterns = [
    path('', home_view),
    path('register/', RegisterView.as_view()),
]

urlpatterns += router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from data import views

router = DefaultRouter()
router.register(r'family', views.FamilyViewSet)

urlpatterns = [
    path('', include(router.urls))
]

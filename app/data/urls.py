from django.urls import path, include
from rest_framework.routers import DefaultRouter
from data import views

router = DefaultRouter()
router.register(r'family', views.FamilyViewSet)
router.register(r'expense', views.ExpenseViewSet)
router.register(r'people', views.PeopleViewSet)

urlpatterns = [
    path('', include(router.urls))
]

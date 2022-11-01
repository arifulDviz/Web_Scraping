from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import Bilbasen_dataViewSet, Biltorvet_dataViewSet, Bilbasen_data_CSV, Biltorvet_data_CSV,  Populating_Bilbasen_data_To_Database, Populating_Biltorvet_data_To_Database

router = DefaultRouter()
router.register('Bilbasen_data', Bilbasen_dataViewSet)
router.register('Biltorvet_data', Biltorvet_dataViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("Populating_Bilbasen_data_To_Database",
         Populating_Bilbasen_data_To_Database),
    path("Populating_Biltorvet_data_To_Database",
         Populating_Biltorvet_data_To_Database),
    path("Bilbasen_data_CSV", Bilbasen_data_CSV),
    path("Biltorvet_data_CSV", Biltorvet_data_CSV),
]

from django.urls import path
from .views import DriversList, DriverDetail, VehicleList, VehicleDetail, VehicleSetDriver

urlpatterns = [
    path('drivers/driver/', DriversList.as_view()),
    path('drivers/driver/<int:pk>', DriverDetail.as_view()),
    path('vehicles/vehicle/', VehicleList.as_view()),
    path('vehicles/vehicle/<int:pk>', VehicleDetail.as_view()),
    path('vehicles/set_driver/<int:pk>', VehicleSetDriver.as_view()),
]

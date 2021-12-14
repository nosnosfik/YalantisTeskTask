from rest_framework.serializers import ModelSerializer
from .models import Driver, Vehicle


class DriverSerializer(ModelSerializer):
    """
        Driver model serializer
    """
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleSerializer(ModelSerializer):
    """
        Vehicle model serializer
    """
    class Meta:
        model = Vehicle
        fields = '__all__'


class SetVehicleDriverSerializer(VehicleSerializer):
    """
        Getting the driver into the car serializer
    """
    class Meta:
        model = Vehicle
        fields = ('driver',)

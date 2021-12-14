import datetime

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer


class DriversList(ListCreateAPIView):
    """
        Get all drivers list, get drivers list by 'created_at' at specified endpoints
    """
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        if self.request.GET.get('created_at__gte'):
            date_gte = datetime.datetime.strptime(self.request.query_params.get('created_at__gte'), '%d-%m-%Y')
            queryset = queryset.filter(created_at__gte=date_gte)
        elif self.request.GET.get('created_at__lte'):
            date_lte = datetime.datetime.strptime(self.request.query_params.get('created_at__lte'), '%d-%m-%Y')
            queryset = queryset.filter(created_at__lte=date_lte)
        return queryset


class DriverDetail(RetrieveUpdateDestroyAPIView):
    """
        Driver get, update, delete methods in model
    """
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class VehicleList(ListCreateAPIView):
    """
        Get all vehicle list, get vehicle list by 'driver' presence or absence in vehicle at specified endpoints
    """
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        with_drivers = self.request.query_params.get('with_drivers')
        if with_drivers == 'yes':
            queryset = queryset.filter(driver__isnull=False)
        elif with_drivers == 'no':
            queryset = queryset.filter(driver__isnull=True)
        return queryset


class VehicleDetail(RetrieveUpdateDestroyAPIView):
    """
        Vehicle get, update, delete methods in model
    """
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class VehicleSetDriver(CreateAPIView):
    """
        Vehicle post method to get driver to the car by id
    """
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    def post(self, request, *args, **kwargs):
        return self.update_car_driver(request, **kwargs)

    def update_car_driver(self, request, **kwargs):
        instance = self.get_object()
        if instance.driver:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            instance.driver = None
            serializer.save()
            return Response({'success': 'a driver out'})
        else:
            try:
                instance.driver = Driver.objects.get(id=int(request.data['driver']))
                serializer = self.get_serializer(instance, data=request.data, partial=kwargs['partial'])
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'success': 'a driver in'})
            except Driver.DoesNotExist:
                return Response({'error': 'a driver with this id does not exist'})

# REST API for car park with drivers.

Database structure and all endpoints of the application are described below.

## Technical stack
+ Python version - 3.10
+ Main framework - Django
+ REST api - DRF
+ Database - SQLite

## Main functionality
This project provides you to GET, POST, UPDATE and DELETE information about drivers
and vehicles. And perform some sorting.

## Endpoint`s

### Driver:
```+ GET /drivers/driver/ - a drivers list
+ GET /drivers/driver/?created_at__gte=10-11-2021 - list of a drivers created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - list of a drivers created before 16-11-2021
+ GET /drivers/driver/<driver_id>/ - get information on a specific driver
+ POST /drivers/driver/ - create new driver
+ UPDATE /drivers/driver/<driver_id>/ - update driver's credentials
+ DELETE /drivers/driver/<driver_id>/ - delete driver
```
### Vehicle:

```+ GET /vehicles/vehicle/ - vehicles list
+ GET /vehicles/vehicle/?with_drivers=yes - list of vehicles with attached driver
+ GET /vehicles/vehicle/?with_drivers=no - list of cars without attached driver
+ GET /vehicles/vehicle/<vehicle_id> - obtaining information on a specific vehicle
+ POST /vehicles/vehicle/ - create new vehicle
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - update vehicle's data
+ POST /vehicles/set_driver/<vehicle_id>/ - get driver in/out the car by id
+ DELETE /vehicles/vehicle/<vehicle_id>/ - delete vehicle
```
from django.db import models
from django.core.validators import RegexValidator


class Driver(models.Model):
    """
        This class represents a Driver model.
    """

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Vehicle(models.Model):
    """
       This class represents a Vehicle model.
    """
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    plate_number = models.CharField(validators=[RegexValidator(
        regex=r'[A-ZА-Я]{2}\s[0-9]{4}\s[A-ZА-Я]{2}',
        message='Incorrect plate number. PN format -> "AA 1111 BB"')],
        max_length=10, unique=True)
    driver = models.ForeignKey(Driver, default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.make} | {self.model} | {self.plate_number}'

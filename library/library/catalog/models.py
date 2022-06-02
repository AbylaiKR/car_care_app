from django.db import models
from django.contrib.auth.models import User

class car_engine(models.Model):

    engine_capacity = models.IntegerField(help_text='Specify the engine volume in cubic centimeters')
    engine_power = models.IntegerField(help_text='Specify the engine power')
    fuel_consumption = models.FloatField(help_text='Specify the fuel consumption per 100 km')

    def __str__(self):
        return f'{self.engine_capacity} {self.engine_power} {self.fuel_consumption}'


class car_transmission(models.Model):
    name = models.CharField(max_length=10, help_text='Enter the car transmission')
    steps_number = models.IntegerField(help_text='Enter the car transmission number of steps')

    def __str__(self):
        return f'{self.name} {self.steps_number}'

class car_modification(models.Model):
    name = models.CharField(max_length=150, help_text='Enter the car model modification name')
    engine = models.ForeignKey(car_engine, on_delete=models.SET_NULL, null=True)
    transmission = models.ForeignKey(car_transmission, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class inner_car_model(models.Model):
    image = models.ImageField()
    inner_model_name = models.CharField(max_length=100, help_text='Enter the inner car model')
    start_production_year = models.IntegerField(help_text='Enter the year of manufacture of the car model')
    end_production_year = models.IntegerField(help_text='Enter the year of the end of the car model release')
    car_modification = models.ManyToManyField(car_modification, help_text='Select a car modification')

    def __str__(self):
        return f'{self.image} {self.inner_model_name} {self.start_production_year} {self.end_production_year}'


class car_body(models.Model):
    name = models.CharField(max_length=150, help_text='Enter the car body name')
    inner_car_model = models.ManyToManyField(inner_car_model, help_text='Select inner car model')

    def __str__(self):
        return self.name

    def display_inner_car_model(self):
        return ', '.join(inner_car_model for inner_car_model in self.inner_car_model.all()[:3])

    display_inner_car_model.short_description = 'Inner car model'


class car_model(models.Model):
    model_name = models.CharField(max_length=100, help_text='Enter the car model')
    car_body = models.ManyToManyField(car_body, help_text='Select a car body')

    def __str__(self):
        return self.model_name

    def display_car_body(self):
        return '.'.join(car_body for car_body in self.car_body.all()[:3])

    display_car_body.short_description = 'Inner car model'


class car_brand(models.Model):
    brand_name = models.CharField(max_length=50, help_text='Enter the car brand')
    car_model = models.ManyToManyField(car_model)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.brand_name

    def display_car_model(self):
        return ', '.join(car_model for car_model in self.car_model.all()[:3])

    display_car_model.short_description = 'Car model'

from django.db import models

import car_variables.choices as cv

# Create your models here.

class Enviornment(models.Model):
    #One-Time Variables
    distance = models.IntegerField("Distance:", default = 0)
    car1_spd = models.IntegerField("Vehicle 1 Speed:", default = 0)
    car2_spd = models.IntegerField("Vehicle 2 Speed:", default = 0)
    road_width = models.IntegerField("Road Width:", default = 0)
    weather = models.IntegerField("Weather:", choices = cv.WEATHER_CHOICES, default = 0)
    time = models.IntegerField("Time:", choices = cv.TIME_CHOICES, default = 1)
    road_type = models.IntegerField("Road Type:", choices = cv.ROAD_CHOICES, default = 1)
    driver_exp1 = models.IntegerField("Driver 1 Experience:", choices = cv.DRIVER_EXP_CHOICES, default = 1)
    driver_exp2 = models.IntegerField("Driver 2 Experience:", choices = cv.DRIVER_EXP_CHOICES, default = 1)
    driver_dui1 = models.IntegerField("Driver 1 Chemical Influence:", choices = cv.DRIVER_DUI_CHOICES, default = 1)
    driver_dui2 = models.IntegerField("Driver 2 Chemical Influence:", choices = cv.DRIVER_DUI_CHOICES, default = 1)
    driver_vision1 = models.IntegerField("Driver 1 Vision:", choices = cv.DRIVER_VISION_CHOICES, default = 1)
    driver_vision2 = models.IntegerField("Driver 2 Vision:", choices = cv.DRIVER_VISION_CHOICES, default = 1)
    driver_age1 = models.IntegerField("Driver 1 Age:", choices = cv.DRIVER_AGE_CHOICES, default = 1)
    driver_age2 = models.IntegerField("Driver 2 Age:", choices = cv.DRIVER_AGE_CHOICES, default = 1)
    vehicle1 = models.IntegerField("Vehicle 1 Type:", choices = cv.VEHICLE_CHOICES, default = 1)
    vehicle2 = models.IntegerField("Vehicle 2 Type:", choices = cv.VEHICLE_CHOICES, default = 1)
    computer = models.IntegerField("AI Computer:", choices = cv.COMPUTER_CHOICES, default = 1)
    
class Drive(models.Model):
    #Repeating Variables
    env = models.ForeignKey(Enviornment,on_delete="cascade")
    car1_prog = models.DecimalField("Vehicle 1 Progress:", max_digits=999, decimal_places=2, default = 0)
    ghost_prog = models.DecimalField("AI Ghost Progress:", max_digits=999, decimal_places=2, default = 0)
    car2_prog = models.DecimalField("Vehicle 2 Progress:", max_digits=999, decimal_places=2, default = 0)
    car1_turndist = models.DecimalField("Vehicle 1 Turn Distance:", max_digits=999, decimal_places=2, default = 0)
    ghost_turndist = models.DecimalField("AI Ghost Turn Distance:", max_digits=999, decimal_places=2, default = 0)
    car2_turndist = models.DecimalField("Vehicle 2 Turn Distance:", max_digits=999, decimal_places=2, default = 0)
    outcome = models.CharField("Outcome:", max_length = 120, default = "")
    accuracy = models.IntegerField("Accuracy:", default = 0)
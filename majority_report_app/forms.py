from django import forms

from .models import Enviornment

class EnviornmentForm(forms.ModelForm):
    class Meta:
        model = Enviornment
        fields = ['distance','car1_spd','car2_spd','road_width','weather','time','road_type','driver_exp1','driver_exp2','driver_dui1','driver_dui2',
                  'driver_vision1','driver_vision2','driver_age1','driver_age2','vehicle1','vehicle2','computer']
        labels = {'distance':'Distance (Meters)',
                  'car1_spd':'Vehicle 1 Speed (MPH)',
                  'car2_spd':'Vehicle 2 Speed (MPH)',
                  'driver1_exp':'Driver 1 Experience',
                  'driver2_exp':'Driver 2 Experience',
                  'driver1_dui':'Driver 1 Chemical Influence',
                  'driver2_dui':'Driver 2 Chemical Influence',
                  'driver1_vision':'Driver 1 Vision',
                  'driver2_vision':'Driver 2 Vision',
                  'driver1_age':'Driver 1 Age',
                  'driver2_age':'Driver 2 Age',
                  'vehicle1':'Vehicle 1 Type',
                  'vehicle2':'Vehicle 2 Type',
                  'computer':'AI Computer',
                  }
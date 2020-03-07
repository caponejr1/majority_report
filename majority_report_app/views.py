from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Enviornment,Drive
from .forms import EnviornmentForm

from car_sim.views import Car, maj_intro, sim_collision, AI
from car_variables.views import Mods,modifiers_intro

def index(request):
    context = {}
    # The Majority Report homepage
    return render(request, 'majority_report_app/index.html', context)

def env_forms(request):
    #Variable Select Page
    if request.method != 'POST':
        form = EnviornmentForm
    else:
        form = EnviornmentForm(data=request.POST)
        if form.is_valid():
            env = form.save()
            return HttpResponseRedirect(reverse('majority_report_app:results', args = [env.id]))
        
    context = {'form': form}
    return render(request, 'majority_report_app/enviornment_variables.html', context)

def results(request,env_id):
    #Return all Variables
    env = Enviornment.objects.get(id=env_id)
    mods = modifiers_intro(env)
    car1 = Car("Car 1",0)
    car2 = Car("Car 2",0)
    Skynet = AI(mods.modify_data["computer"][mods.modify_choices["computer"]]["name"],mods.modify_data["computer"][mods.modify_choices["computer"]]["comp_power"])
    maj_intro(car1,car2,env)
    sim_collision(car1,car2,Skynet,mods,env)
    context = {'var': env}
    return render(request, 'majority_report_app/results.html', context)
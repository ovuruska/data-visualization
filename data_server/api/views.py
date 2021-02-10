from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import History
from .JetDataset import JetDataset
from functools import wraps
from random import randint
from json import loads,dumps

# Create your views here.

def func(f):

    dataset = JetDataset()

    @wraps(f)
    def wrapper(*args,**kwargs):

        return f(*args,**kwargs,dataset=dataset)

    return wrapper

@func
def data(request,dataset = None):
    history = History().load()

    if history.history == "":
        history.history = "[]"

    prev_values = loads(history.history)
    ind = randint(0,len(dataset))
    prev_values.append(ind)
    history.history = dumps(prev_values)

    history.save()

    particles = dataset[ind]


    return JsonResponse({
        "index":ind,
        "particles":particles.tolist()
    })


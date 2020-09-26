from django.shortcuts import render
from .bubble_sort import BubbleSort
import random
from django.http import QueryDict
from django import forms

# Create your views here.

arr = []


def setarray():
    arr.clear()
    for i in range(26):
        arr.append(random.randrange(1, 1000))


def home(request):

    if request.method == "POST":
        if request.POST.get('resetarray'):
            setarray()
            return render(request, 'visualizer/home.html', {'array': arr})
        elif request.POST.get('sortarray-bubblesort'):
            yielded_output = BubbleSort(arr).sort()
            for a in yielded_output:
                return render(request, 'visualizer/home.html', {'array': a})
    else:
        context = {'title': 'Home',
                   'array': arr,
                   }
        return render(request, 'visualizer/home.html', context)


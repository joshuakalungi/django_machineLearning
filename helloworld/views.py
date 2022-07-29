from django.shortcuts import render
from . import machine_learning

def home(request):
    return render(request, 'index.html'
       )

def about(request):
    return render(request ,'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def operations(request):
    return render(request, 'operations.html')

def missingValues(request):
    return render(request, 'missingValues.html')

def dataCleaning(request):
    return render(request, 'dataCleaning.html')

def result(request):
    user_input = request.GET['user_input']
    user_input = machine_learning.multiplier(user_input)
    return render(request, 'results.html', {'home_input':user_input} 
    )
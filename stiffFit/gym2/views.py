from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
def home(request):
    context={}
    return render(request,'gym2/home.html', context)

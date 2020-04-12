from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import RetailerForm

# Create your views here.

def index(request):
    return render(request, 'contributors/index.html')




from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse



# @login_required
def index(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'index.html', {})

def showContact(request):
    return render(request, 'index.html', {})

def personalPage(request):
    return render(request, 'index.html', {})
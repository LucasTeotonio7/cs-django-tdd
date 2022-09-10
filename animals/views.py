from django.shortcuts import render
from django.http import HttpResponse
from animals.models import Animal

# Create your views here.

def index(request):
    context = { 'characteristics': Animal.objects.all() }
    return render(request, 'index.html', context)

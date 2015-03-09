from django.shortcuts import render
from .forms import TaxiGroupForm

def index(request):
	return render(request, 'index.html', {})

def matchtime(request):
	form = TaxiGroupForm()
	return render(request, 'matchtime.html', {'form': form})


def groupinfo(request):
	return render(request, 'groupinfo.html',{})
from django.shortcuts import render

def index(request):
	return render(request, 'index.html', {})

def matchtime(request):
	return render(request, 'matchtime.html', {})

from django.shortcuts import render
from .forms import TaxiGroupForm
import datetime

def index(request):
    return render(request, 'index.html', {})

def matchtime(request):
    form = TaxiGroupForm()
    if request.method == "POST":
        form = TaxiGroupForm(request.POST)
        Group = form.save(commit = False)
        Group.date = datetime.datetime.now()
        Group.time = datetime.datetime.now()
        Group.num_ppl = 2

        Group.save()
    else:
        form = TaxiGroupForm()

    return render(request, 'matchtime.html', {'form': form})


def groupinfo(request):
    return render(request, 'groupinfo.html',{})
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import TaxiGroupForm
import datetime

def index(request):
    form = TaxiGroupForm()
    if request.method == "POST":
        form = TaxiGroupForm(request.POST)
        Group = form.save(commit = False)
        Group.date = datetime.datetime.now()
        Group.time = datetime.datetime.now()
        Group.num_ppl = 2

        Group.save()
        return redirect('matchtime/', pk=Group.pk)
    else:
        form = TaxiGroupForm()
    return render(request, 'index.html', {'form': form})

def matchtime(request):
    return render(request, 'matchtime.html', {})


def groupinfo(request):
    return render(request, 'groupinfo.html',{})
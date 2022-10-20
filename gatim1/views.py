from operator import is_
from django.shortcuts import render, redirect
from .models import Retete
from .models import Members
from .forms import MemberForm 

def index(request):
    # all_members = Members.objects.all
    # return render(request, 'index.html', {'all':all_members})
    # if request.method == "POST":
    #     form = MemberForm(request.POST or None)
    #     if form.is_valid():
    #         members = form.save()
    #         members.refresh_form_db()
    #         members.save()            
    #     return redirect('index.html', {})
    # else:
    #     form = Members()
        return render(request, 'index.html', {})

def condimente(request):
    return render(request, 'condimente.html', {})

def blog(request):
        return render(request, 'blog.html', {})

def retete(request):
    retete_ok = Retete.objects.all().order_by('date')
    return render(request, 'retete.html', {'retete_ok':retete_ok})

def join(request):
    return render(request, 'index.html', {})
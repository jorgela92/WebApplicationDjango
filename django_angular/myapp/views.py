from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from .models import Register
from .forms import RegisterForm

# Create your views here.
from django.shortcuts import render

def home(req):
    all_register = Register.objects.all()
    return render(req, 'main.html', {'STATIC_URL': settings.STATIC_URL, 'all_register': all_register})

def new(req):
    if req.method == 'POST':
        print('post')
        form = RegisterForm(data=req.POST)
        print(form)
        if form.is_valid():
            print('is valid')
            form.save()
            return HttpResponseRedirect('/')
        else:
            print('no valido')
            return render(req, 'new.html', {'STATIC_URL': settings.STATIC_URL, 'form': RegisterForm()})
    else:
        return render(req, 'new.html', {'STATIC_URL': settings.STATIC_URL, 'form': RegisterForm()})

from django.shortcuts import render, redirect

from customers.forms import CustomerForm
from customers.models import Customer


# Create your views here.


def index(request):
    return render(request, template_name='index.html')

def about(request):
    return render(request, template_name='about.html')



def contact(request):
    if request.method == 'POST':
      form = CustomerForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        return redirect('contact')
    else:
        form = CustomerForm()
    return render(request, template_name='contact.html', context={'form':form})

def home(request):
    return render(request, template_name='home.html')

def gallery(request):
    return render(request, template_name='gallery.html')


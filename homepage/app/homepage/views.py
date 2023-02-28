from django.shortcuts import render, redirect
from .forms import DeliveryRequestForm
from .models import DeliveryRequest
from .models import Truck


def home(request):
    trucks = Truck.objects.all()
    return render(request, 'exchange_app/home.html', {'trucks': trucks})


def delivery_request(request):
    if request.method == 'POST':
        form = DeliveryRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeliveryRequestForm()
    return render(request, 'exchange_app/delivery_request.html', {'form': form})

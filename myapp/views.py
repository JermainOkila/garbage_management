
from django.shortcuts import render, redirect
from .models import PickupRequest
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def request_pickup(request):
    if request.method == 'POST':
        location = request.POST['location']
        waste_type = request.POST['waste_type']
        description = request.POST['description']

        PickupRequest.objects.create(
            user=request.user,
            location=location,
            waste_type=waste_type,
            description=description
        )
        return redirect('my_requests')

    return render(request, 'request.html')


@login_required
def my_requests(request):
    requests = PickupRequest.objects.filter(user=request.user)
    return render(request, 'my_requests.html', {'requests': requests})
def home(request):
    return render(request, 'home.html')

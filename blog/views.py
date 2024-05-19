from django.shortcuts import render, redirect, get_object_or_404
from .models import UserInfo
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import userform
# Create your views here.

# Homepage
def home(request):
    return render(request, 'blog/index.html')

#about page
def about(request):
    return render(request, 'blog/about.html')

#Users page
@login_required
def user(request):
    userInfos = UserInfo.objects.all().order_by['data']
    context = {
        'userInfos':userInfos
    }
    models = UserInfo
    if request.method == 'POST':
        users = request.Post['user']
        pet_names = request.POST['pet_name']
        dates = request.POST['date']
        times = request.POST['time']
        messages.success(request, 'You have booked an appointment successfully!')
        return render(request, "blog/message.html",{
            'users' : users,
            'pet_names' : pet_names,
            'dates' : dates,
            'times' : times,})
    else:
        return render(request, "blog/user.html",context)

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(userInfo, id=booking_id, user=request.user)
    booking.delete()
   
@login_required
def appointment(request):
    return render(request, 'blog/appointment.html')

@login_required
def message(request):
    return render(request, 'blog/message.html')

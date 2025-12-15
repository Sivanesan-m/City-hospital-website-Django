from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient, Appointment

def home(request):
    return render(request, 'home.html')

def user_login(request):
    error = ""
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid login details"
    return render(request, 'login.html', {'error': error})

@login_required(login_url='/login/')
def dashboard(request):
    if hasattr(request.user, 'doctor'):
        appointments = Appointment.objects.filter(doctor=request.user.doctor)
        return render(request, 'doctor_dashboard.html', {'appointments': appointments})

    if hasattr(request.user, 'patient'):
        appointments = Appointment.objects.filter(patient=request.user.patient)
        return render(request, 'patient_dashboard.html', {'appointments': appointments})

    return render(request, 'admin_dashboard.html')

@login_required(login_url='/login/')
def book_appointment(request):
    doctors = Doctor.objects.all()
    if request.method == "POST":
        Appointment.objects.create(
            doctor_id=request.POST['doctor'],
            patient=request.user.patient,
            date=request.POST['date'],
            time=request.POST['time']
        )
        return redirect('dashboard')
    return render(request, 'appointment.html', {'doctors': doctors})

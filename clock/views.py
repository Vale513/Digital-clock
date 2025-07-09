from django.shortcuts import render

# Create your views here.
def digital_clock(request):
     return render(request, 'clock/clock.html')
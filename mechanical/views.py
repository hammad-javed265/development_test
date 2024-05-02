from django.shortcuts import render

def mechanical(request, equipment):
    return render(request, 'mechanical/mechanical.html', {'equipment': equipment})
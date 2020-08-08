from django.shortcuts import render, HttpResponse
from .models import Kimchi


# Create your views here.
def home(request):
    return render(request, 'kimchis/home.template.html')


def all_kimchis(request):
    kimchis = Kimchi.objects.all()
    return render(request, 'kimchis/all_kimchis.template.html', {
        'kimchis': kimchis
    })

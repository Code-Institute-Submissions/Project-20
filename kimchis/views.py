from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib.auth.models import auth
from .models import Kimchi


def home(request):
    return render(request, 'kimchis/home.template.html')


def all_kimchis(request):
    kimchis = Kimchi.objects.all()
    return render(request, 'kimchis/all_kimchis.template.html', {
        'kimchis': kimchis
    })


def kimchi_details(request, kimchi_id):
    kimchi = get_object_or_404(Kimchi, pk=kimchi_id)
    return render(request, 'kimchis/kimchi_details.template.html', {
        'kimchi': kimchi
    })


def logout(request):
    auth.logout(request)
    return redirect(reverse(home))

from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Kimchi


# Create your views here.
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



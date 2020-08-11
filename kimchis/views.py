from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib.auth.models import auth
from django.db.models import Q
from .forms import SearchForm
from .models import Kimchi


def home(request):
    form = SearchForm(request.GET)

    if request.GET:
        queries = ~Q(pk__in=[])

        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            queries = queries & Q(title__icontains=title)

        if 'main_ingredient' in request.GET and request.GET['main_ingredient']:
            main_ingredient_id = request.GET['main_ingredient']
            queries = queries & Q(main_ingredient=main_ingredient_id)

        kimchis = Kimchi.objects.all()
        kimchis = kimchis.filter(queries)
        return render(request, 'kimchis/home.template.html', {
            'form': form,
            'kimchis': kimchis
        })
    else:
        kimchis = Kimchi.objects.all()
        return render(request, 'kimchis/home.template.html', {
            'form': form,
            'kimchis': kimchis
        })


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


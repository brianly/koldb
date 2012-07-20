# Create your views here.
from koldb.models import Kol
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    kol_list = Kol.objects.all()
    kol_list_international = Kol.objects.filter(international='Yes').all()
    params = {
        'kol_list': kol_list,
        'kol_list_international': kol_list_international
    }
    return render_to_response('index.html', params)

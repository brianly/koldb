# Create your views here.
from koldb.models import Kol
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

def index(request):
    kol_list = Kol.objects.all().order_by('first_name')
    t = loader.get_template('kols.html')
    c = Context({
        'kol_list': kol_list,
    })
    return HttpResponse(t.render(c))

def detail(request, kol_id):
    try:
        k = Kol.objects.get(pk=kol_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'kol': k})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)













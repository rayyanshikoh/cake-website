from django import template
from django.http.response import Http404
from .models import Cake
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    latest_cakes_list = Cake.objects.order_by('-pub_date')
    # template=loader.get_template('cakes/index.html')
    context = {'latest_cakes_list':latest_cakes_list}
    return render(request, 'cakes/index.html', context)
    # return HttpResponse(template.render(context, request))

def detail(request, cake_id):
    # return HttpResponse("You're looking at cake %s." % cake_id)
    # try:
    #      cake = Cake.objects.get(pk=cake_id)
    # except Cake.DoesNotExist:
    #     raise Http404("Cake not found")
    # return render(request, 'cakes/detail.html', {'cake':cake})
    cake = get_object_or_404(Cake, pk=cake_id)
    return render(request, 'cakes/detail.html', {'cake':cake})

def order(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)
    return render(request, 'cakes/order.html', {'cake':cake})

def comporder(request, cake_id):
    # cake = request.POST.get("cake_id")
    cake = get_object_or_404(Cake, pk=cake_id)
    email_id = request.POST.get("email_id")
    number = request.POST.get("number")
    name = request.POST.get("name")
    print(f"{name} ordered {cake} with the email {email_id}")
    return HttpResponse("order successful")
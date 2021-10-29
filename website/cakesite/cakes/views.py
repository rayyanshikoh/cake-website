from django import template
from django.http.response import Http404
from .models import Cake
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from cakesite.settings import EMAIL_HOST_USER
import random

from .fileprep import deleter, new_writer

header = ("Order_Num", "Cake", "Name", "Email", "Phone")
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

filename = "orders.csv"

def comporder(request, cake_id):
    # cake = request.POST.get("cake_id")
    cake = get_object_or_404(Cake, pk=cake_id)
    email_id = request.POST.get("email_id")
    number = request.POST.get("number")
    name = request.POST.get("name")
    order_num = str(random.randint(1000, 9999))
    print(f"{name} ordered {cake} with the email {email_id}, order number: {order_num}")
    try:
        print("Attempting to add to CSV file")
        new_writer(filename, header, name=name, email=email_id, phone=number, cake=cake, order_num=order_num)
        print("Successfully Added")
        try:
            print("Attempting to send email")
            send_mail("Order Confirmation", f"{name}! Thanks for ordering {cake.name}. \n You have succesfully placed an order for {cake.name} order number is {order_num}, we will contact you shortly via your provided phone number: {number}", EMAIL_HOST_USER, [email_id], fail_silently=False)
            print("Email Sent!")
            return render(request, 'cakes/successful_order.html', {'order_num':order_num})
        except:
            print("Email Failed")
            deleter(filename, order_num)
            print("Deleted!")
            return HttpResponse("Order Unsuccessful!")
    except:
        return HttpResponse("Order Unsuccessful, Please try again later!")
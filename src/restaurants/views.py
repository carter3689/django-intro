import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based views
def home(request):
    num = random.randint(0,10000000)
    some_list = [random.randint(0,200000),random.randint(0,3000000)]
    context = {"num": num,
    "bool_item":True,
    "some_item":some_list
    }
    return render(request, "base.html",context )#response

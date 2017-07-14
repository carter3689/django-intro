from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based views
def home(request):
    html_ = """<!DOCTYPE html>
    <html lang = en>

    <head>
    </head>
    <body>
    <h1> Hello World </h1>
    <p> This is html coming through here.</p>
    </body>
    </html>
    """
    return HttpResponse(html_)
    #return render(request, "home.html", {})#response

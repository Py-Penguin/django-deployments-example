from django.shortcuts import render
from random import randint

# Create your views here.
def index(request):
    context_dict = {'text':'Hello World', 'number':randint(0,1000)}
    return render(request, "AppNumber4/index.html", context_dict)

def other(request):
    return render(request, "AppNumber4/other.html")

def relative(request):
    return render(request, "AppNumber4/relative_url_templates.html")
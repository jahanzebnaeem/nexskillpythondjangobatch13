from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Welcome to the class</h1>")
    # return render(request, "index.html")
    context = {"myMsg":"Hello how are you"}
    return render(request, "first_app/index.html", context)

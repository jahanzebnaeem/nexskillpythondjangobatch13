from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Welcome to the class</h1>")
    # return render(request, "index.html")
    # context = {"myMsg":"Hello how are you"}
    # return render(request, "first_app/index.html", context)
    topic_list = Topic.objects.all()
    topic_list_dict = {'topic_dict':topic_list}
    return render(request, "first_app/index.html", topic_list_dict)
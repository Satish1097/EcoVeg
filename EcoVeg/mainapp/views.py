from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def Home(req):
    return render(req,'index.html')
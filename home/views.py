from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm , SubsForm

# Create your views here.
def home(request):
    return render(request, 'index.html' , {})


def sub(request):
       


    if request.method == "POST":

        form = SubsForm(request.POST)
        if form.is_valid() :
            form.save()

            data = {'ok' : 'ok'}
                
            return JsonResponse(data)

   


def contact(request):
       


    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
                
            return JsonResponse({
                'msg': 'Success'
                })


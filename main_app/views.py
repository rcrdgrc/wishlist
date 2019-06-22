from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import List


class ListCreate(CreateView):
    model = List
    fields = '__all__'
    success_url = '/'

class ListDelete(DeleteView):
    model = List
    success_url = '/'


def home(request):
    lists = List.objects.all()
    return render(request, 'home.html', {
        'lists': lists
    })



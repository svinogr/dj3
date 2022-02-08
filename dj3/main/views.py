from django.shortcuts import render
from .models import Group
from django.views.generic import DetailView
# Create your views here.

class DetailsGroup(DetailView):
    DetailView.model = Group
    DetailView.template_name = 'main/details_group.html'
    DetailView.context_object_name = 'group'


def group(request):
    data = Group. objects.all()
    return render(request, 'main/group.html', {'data': data})


def index(request):
    return render(request, 'main/index.html')

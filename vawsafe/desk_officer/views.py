from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'desk_officer/index.html')

def victim_list(request):
    return render(request, 'desk_officer/victim_tab/victim_list.html')

# social worker views
def social_worker_list(request):
    return render(request, 'desk_officer/social_worker_tab/list_social_worker.html')

def add_social_worker(request): 
    return render(request, 'desk_officer/social_worker_tab/add_social_worker.html')

def social_worker_case(request):
    return render(request, 'desk_officer/social_worker_tab/social_worker_case.html')
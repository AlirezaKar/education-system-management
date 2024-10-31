from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def api_view(request):  
    return JsonResponse({'title':'123'})
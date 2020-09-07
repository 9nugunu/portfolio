from django.shortcuts import render
from .models import Portfoilo
# Create your views here.

def portfolio(request):
    portfolio = Portfoilo.objects
    return render(request, 'portfolio.html', {'portfolios': portfolio.all})
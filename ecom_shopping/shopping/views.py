from django.shortcuts import render

# Create your views here.
from store.models import Product

def index(request):
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products': products,
    }
    
    return render(request, 'shopping/index.html', context)

from django.shortcuts import render
from item.models import Item, Category
# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'items': items,
        'categories': categories,
    })


def contact(request):
    return render(request, 'core/contact.html')


def terms(request):
    return render(request, 'core/terms.html')

def about(request):
    return render(request, 'core/about.html')

def policy(request):
    return render(request, 'core/policy.html')

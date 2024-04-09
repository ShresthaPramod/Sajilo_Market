from django.shortcuts import render, redirect

from item.models import Category, Item
from .forms import SignupForm

def items(request):
    query = request.GET.get('query', '')
    items =  Item.objects.filter()

    if query:
        items =items.filter(name__icontains=query)

    return render(request, 'Item/items.html',{
        'items':items,
        'query':query,
    }) 

def index(request):
    items = Item.objects.filter()
    categories = Category.objects.all()

    return render(request, 'market/index.html',{
        'categories':categories, 
        'items':items,
    })
# Create your views here.
def contact(request):
    return render(request, 'market/contact.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'market/signup.html',{
        'form' : form,
    })
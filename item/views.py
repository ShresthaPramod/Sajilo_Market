from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm,EditItemForm
from .models import Category, Item
# Create your views here.
# def items(request):
#     items =  Item.objects.filter()

#     return render(request, 'item/items.html',{
#         'items':items
#     }) 




def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'item/detail.html',{
        'item': item,
    })
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
             item = form.save(commit= False)
             item.save()
             return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item'
    })  

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
     
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()

    return redirect('market:items')                   



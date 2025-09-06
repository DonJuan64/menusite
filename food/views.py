from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader 
from .forms import ItemForm



def index(request):
    item_list = Item.objects.all()
   
    context = {
        'item_list':item_list,
    }



    return render(request,'food/index.html',context)





def item(request):
    return HttpResponse('<h1>This is an item view</h1>')



def detail(request,item_id):
    item_detail = Item.objects.get(pk=item_id)
    context = {
        'item_detail':item_detail,
    }
    return render(request,'food/detail.html',context)



def create_item(request):
    form = ItemForm(request.POST or None )

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form} )




def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form, 'item':item})
    #form is returned for context but the item data also needs to be edited thats why i also pass it into the context so that its passed to the form to be able to be edited 

def delete_item(request, id):
    #id on top is us getting the id of the item to than be able to use an object to access that specfic item with the same id thats why id = id 
    item = Item.objects.get(id=id)

    if request.method == 'POST': 
        item.delete()
        return redirect('food:index')
    #this is for a template making sure that is the item we want to delete and we have to pass in item as the context so it shows up from the database and shows us which item we want to delete 
    return render(request,'food/item-delete.html', {'item':item})














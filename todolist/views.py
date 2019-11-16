from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Item

def main(request):
    if request.user.is_authenticated:
        items = Item.objects.all().filter(responsable_id=request.user.id).order_by('id')
        return render(request,'main.html', {'items':items})
    return render(request,'main.html')


def registrar_item(request):
    item = Item(descripcion=request.POST['descripcion'], completado=request.POST.get('completado',False), responsable_id=request.user.id)
    item.save()
    return redirect('/')


def actualizar_item(request):
    item = Item.objects.get(id=request.POST['item_id'])
    item.descripcion = request.POST['descripcion']
    item.completado = request.POST.get('completado',False)
    item.save()
    return redirect('/')


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('/')
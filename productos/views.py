from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto


productos=[]

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})


def agregar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        descripcion = request.POST.get("descripcion")
        Producto.objects.create(nombre=nombre, precio=precio, descripcion=descripcion) 
        return redirect('productos:listar_productos')
    return render(request, "agregar.html")

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        
        # Actualiza los campos del producto
        producto.nombre = nombre
        producto.precio = precio
        producto.descripcion = descripcion
        producto.save()
        
        return redirect('productos:listar_productos')
    else:
        return render(request, 'actualizar.html', {'producto': producto})



def eliminar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        try:
            producto = Producto.objects.get(nombre=nombre)
            producto.delete()
        except Producto.DoesNotExist:
            pass
        
        return redirect('productos:listar_productos')
    return render(request, "eliminar.html")


def buscar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        try:
            producto = Producto.objects.get(nombre=nombre)
            return render(request, "buscar.html", {"producto": producto})
        except Producto.DoesNotExist:
            return render(request, "buscar.html", {"producto": None})
    return render(request, "buscar.html")
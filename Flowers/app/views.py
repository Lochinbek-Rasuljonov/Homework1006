from django.shortcuts import render, get_object_or_404, redirect
from .models import Flower, Type
from .forms import FlowerForm

def base(request):
    return render(request, 'base.html')

def all_flowers(request):
    flowers = Flower.objects.select_related('type').all()
    return render(request, 'flowers/all_flowers.html', {'flowers': flowers})

def flowers_by_type(request, type_id):
    flowers = Flower.objects.filter(type_id=type_id)
    return render(request, 'flowers/flowers_by_type.html', {'flowers': flowers})

def single_flower(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flowers/single_flower.html', {'flower': flower})

def add_flower(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_flowers')
    else:
        form = FlowerForm()
    return render(request, 'flowers/add_flower.html', {'form': form})
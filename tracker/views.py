from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Food, Consume

@login_required
def index(request):
    if request.method == 'POST':
        if 'food' in request.POST:
            food_consumed = request.POST['food']
            food = Food.objects.get(name=food_consumed)
            user = request.user
            consume = Consume(user=user, food_consumed=food)
            consume.save()
            return redirect('index')
    foods = Food.objects.all()
    consumed = Consume.objects.filter(user=request.user)
    consumed_calories = 0
    for consume in consumed:
        consumed_calories += consume.food_consumed.calories
    return render(request, 'tracker/index.html', {'foods': foods, 'consumed_calories': consumed_calories})  
    
@login_required
def add_food(request):
    if request.method == 'POST':
        food = Food(name=request.POST['name'], carbs=request.POST['carbs'], protein=request.POST['protein'], fats=request.POST['fats'], calories=request.POST['calories'])
        food.save()
        return redirect('index')
    return render(request, 'tracker/add_food.html')
    
@login_required
def delete_consumed(request, consumed_id):
    consumed = get_object_or_404(Consume, id=consumed_id)
    if request.method == 'POST':
        consumed.delete()
        return redirect('index')
    return render(request, 'tracker/delete_consumed.html', {'consumed': consumed})

@login_required
def delete_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        food.delete()
        return redirect('index')
    return render(request, 'tracker/delete_food.html', {'food': food})

@login_required
def delete_item(request, id):
    item = get_object_or_404(Food, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'tracker/delete.html', {'item': item})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
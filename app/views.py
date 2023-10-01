from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

"""Это мой валидатор, принимает только положительные числа."""

def drinks_view(request):
    drinks = Drinks.objects.all()
    context = {'drinks':drinks}
    return render(request, 'home.html', context)

def create_drinks(request):
    if request.method == "POST":
        one = request.POST
        if int(one['value']) >= 0:
            drink = Drinks.objects.create(name=one['name'], value=one['value'])
            drink.save()
            return redirect('home')
        else:
            return HttpResponse("Введите положительное число")
    else:
        return render(request, 'create.html')

"""Тут я решил сделать квадратный калькулятор, первое число вводите вы, второе число в таблицу вставляет функция."""

def square_view(request):
    square = Square.objects.all()
    context = {'square':square}
    return render(request, 'numbers.html', context)

def create_square(request):
    if request.method == "POST":
        new_number = request.POST
        new_square = Square.objects.create(number=new_number['number'], numbers_square=int(new_number['number'])**2)
        new_square.save()
        return redirect('numbers')
    else:
        return render(request, 'insertnumbers.html')
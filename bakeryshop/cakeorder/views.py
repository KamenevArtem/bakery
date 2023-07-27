from django.shortcuts import render, loader, HttpResponse
from .models import Levels_number, Form, Topping, Berries, Decor


def index(request):
    levels = Levels_number.objects.all()
    forms = Form.objects.all()
    toppings = Topping.objects.all()
    berries = Berries.objects.all()
    decors = Decor.objects.all()

    context = {
        'data': {
            'levels': [level.quantity for level in levels],
            'forms': [{'id': form.id, 'name': form.name} for form in forms],
            'toppings': [{'id': topping.id, 'name': topping.name} for topping in toppings],
            'berries': [{'id': berry.id, 'name': berry.name} for berry in berries],
            'decors': [{'id': decor.id, 'name': decor.name} for decor in decors],
        },
        'costs': {
            'levels': [0] + [level.price for level in levels],
            'forms': [0] + [form.price for form in forms],
            'toppings': [0] + [topping.price for topping in toppings],
            'berries': [0] + [berry.price for berry in berries],
            'decors': [0] + [decor.price for decor in decors],
        }
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))


def lk(request):
    context = {}
    template = loader.get_template('lk.html')
    return HttpResponse(template.render(context))


def lk_order(request):
    context = {}
    template = loader.get_template('lk-order.html')
    return HttpResponse(template.render(context))

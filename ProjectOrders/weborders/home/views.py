import json

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, Http404, JsonResponse
from django.shortcuts import redirect, render

from home.OrderService import *


def index(request):
    context = {
        'orders': getAllOrders()
    }
    return render(request, 'index.html', context)


def order(request, git):
    data = {
        'orders': getOrdersByGit(git)
    }
    return JsonResponse(data)
#return redirect('home', permanent=False)

def pageNotFound(request, exception):
    print(request.GET)
    return HttpResponseServerError(f"<h1>Страница не найдена</h1>")
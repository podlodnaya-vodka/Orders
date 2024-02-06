from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('index/', index),
    path('order/<int:git>/', order)
]


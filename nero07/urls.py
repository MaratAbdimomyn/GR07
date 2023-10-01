from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', drinks_view, name='home'),
    path('create', create_drinks, name='create'),
    path('numbers', square_view, name='numbers'),
    path('square', create_square, name='square')
]
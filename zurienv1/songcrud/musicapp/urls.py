from django.urls import path
from . import views # imported from this current folder

# URLconf = URL configuration model
urlpatterns = [
    path('hello/', views.sayHello) # musicapp/ is removed because it is added in the proj urls.py
]

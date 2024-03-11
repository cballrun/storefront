from django.urls import path
from . import views

#URLConf module, every app can have its own, but we have to import it into the main URL configuration
urlpatterns = [
    path('hello/', views.say_hello)
]
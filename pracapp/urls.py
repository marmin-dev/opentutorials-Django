from django.urls import path
from pracapp import views

urlpatterns = [
    path('', views.index),

]

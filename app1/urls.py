from django.urls import path
from . import views

urlpatterns = [
    path('hi/<str:name>/<int:age>/', views.say_hi),
]
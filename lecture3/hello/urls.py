from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cakir",views.cakir,name="cakir"),
    path("<str:name>",views.greet,name="greet")
]
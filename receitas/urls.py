from django.urls import path

from . import views

urlpatterns = [
    path('', views.home), #Home
    path('receitas/<int:id>/', views.receitas)
]

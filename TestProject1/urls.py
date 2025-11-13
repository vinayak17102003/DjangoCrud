from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.show_details, name = 'create'),
    path('update/<int:id>/',views.update_details, name = 'update'),
    path('delete/<int:id>/',views.delete_details, name = 'delete'),
]
    
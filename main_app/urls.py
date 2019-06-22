from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.ListCreate.as_view(), name='lists_create'),
    path('<int:pk>/delete/', views.ListDelete.as_view(), name='lists_delete'),
]


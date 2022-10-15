from django.urls import path
from MyRestApi import views

urlpatterns = [
    path('apilist/', views.api_list),
    path('apidetail/<int:pk>/', views.api_detail),
]
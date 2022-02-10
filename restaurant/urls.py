from django.urls import path
from .views import DashboardView, OrderDetailsView


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('orders/<int:pk>/', OrderDetailsView.as_view(), name='order-details'),
]

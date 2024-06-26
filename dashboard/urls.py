from django.urls import path 
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.DashboardView.as_view(), name = "homepage"),
    path("place-order/", views.PlaceOrder.as_view(), name = "place_order")
]
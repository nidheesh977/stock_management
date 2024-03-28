from django.shortcuts import render, redirect
from django import views
from .models import Orders

from rest_framework import views, permissions, response

# Create your views here.


class DashboardView(views.View):
    def get(self, request):

        if not request.user.is_authenticated:
            return redirect("account:login")

        orders = Orders.objects.all()
        sold = orders.filter(order_status = "delivered")
        cancelled = orders.filter(order_status = "cancelled")

        profit = 0
        for order in sold:
            profit+=order.product.price

        loss = 0
        for order in cancelled:
            loss+=order.product.price

        new_orders = orders.filter(order_status = "pending")

        context = {
            "total_stock": len(orders),
            "total_sales": len(sold),
            "profit": profit,
            "loss": loss,
            "new_orders": new_orders,
        }

        return render(request, "dashboard/index.html", context)
    
class PlaceOrder(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        Orders.objects.create(
            buyer = request.user,
            product = request.data["product"],
            order_status = "pending",
        )

        return response({"status": "Ordered successfully"})
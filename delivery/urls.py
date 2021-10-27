from django.urls import path
from .views import (
    BranchListView,
    StatusListView,
    OrderListView,
    OrderDetailView
    )

urlpatterns = [
    path("branches/", BranchListView.as_view(), name="branch-list"),
    path("statuses/", StatusListView.as_view(), name="status-list"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("order-detail/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
]
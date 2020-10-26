from django.urls import path
from .views     import ProductDetailView

urlpatterns = [
        path('/productdetail', ProductDetailView.as_view())
]

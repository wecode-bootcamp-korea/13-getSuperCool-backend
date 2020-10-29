import json

from django.views import View
from django.http  import HttpResponse, JsonResponse

from products.models import Product
from orders.models   import Order, OrderItem, OrderStatus

class CartView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        for item in data:
            product_id
            color_id
            quantity
            price
            모델 바꾸고(color id 추가)

        order create 
        user_id
        order_number
        order_status_id = 1
            

        return JsonResponse({"message" : "UPDATED SHOPPING CART"}, status =201)






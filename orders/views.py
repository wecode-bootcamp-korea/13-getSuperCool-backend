import json

from django.views import View
from django.http  import HttpResponse, JsonResponse

from products.models import ProductColor, Product, Color, Image
from orders.models   import Order, OrderItem, OrderStatus
from users.authorization import token_check

class CartView(View):
    @token_check
    def post(self, request):
        data = json.loads(request.body)
        
        user_id    = request.user.id
        product_id = data['product_id'] 
        color_id   = data['color_id'] if data['color_id'] != '' else None 
        quantity   = data['quantity']
        
        order = Order.objects.get_or_create(user_id=user_id, order_status_id=1)[0]
        
        product_color =  ProductColor.objects.get(product_id=product_id, color_id=color_id)
        
        order_item = OrderItem.objects.get_or_create(order_id=order.id, productcolor_id=product_color.id)[0]
        order_item.quantity = quantity
        order_item.save()
        
        items_in_cart = OrderItem.objects.filter(order_id=order.id).select_related('productcolor__product','productcolor__color')

        item_list = [{
            'product_name': item.productcolor.product.name,
            'color_name': item.productcolor.color.name if item.productcolor.color_id else '',
            'quantity': item.quantity 
            } for item in items_in_cart]     

        return JsonResponse({"items_in_shopping_cart" : item_list}, status =201)






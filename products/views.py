import json

from django.views import View
from django.http  import HttpResponse, JsonResponse

from products.models import Product, Color, ProductImage

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            color_id = request.GET.get('color_id', None)
            
            product = Product.objects.get(id=product_id)

            images = product.productimage_set.filter(color_id=color_id)
            product_images = [image.image_url for image in images]
            
            if color_id:
                color_ids = product.productimage_set.values_list('color_id',flat=True).distinct()
                color_options = [{"id": id, "name": Color.objects.get(id=id).name} for id in color_ids]
            else:
                color_options = []
            
            product_info = Product.objects.filter(id = product_id).values()

            product_detail = {
                "product_images" : product_images,     
                "color_options" : color_options,
                "product_info" : product_info[0],
            }

            return JsonResponse({"product_detail" : product_detail}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "Product does not exist"}, status=400)

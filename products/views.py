import json

from django.views import View
from django.http  import HttpResponse, JsonResponse

from products.models import Product, Color, ProductImage

class ProductDetailView(View):
    def get(self, request):
        try:
            product_id = request.GET['product_id']
            color_id = request.GET.get('color_id', None)
            
            images_of_product_id = ProductImage.objects.filter(product_id=product_id)

            if color_id:
                images = images_of_product_id.filter(color_id=color_id).values_list('image_url',flat=True)
                other_color_ids = images_of_product_id.values_list('color_id',flat=True).distinct()
                color_options = {id:Color.objects.get(id=id).name for id in other_color_ids}
            else:
                images = images_of_product_id.values_list('image_url',flat=True)
                color_options = {}

            product_info = list(Product.objects.filter(id=product_id).values())
            product_images = list(images)
            
            product_detail = [{
                "color options" : color_options,
                "product images" : product_images,
                "product info" : product_info,
            }]

            return JsonResponse({"product detail": product_detail}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({"message": "Product doesn't exist"}, status=400)

import json

from django.views     import View
from django.http      import HttpResponse, JsonResponse
from django.db.models import Q

from products.models import Product, Color, ProductImage, Category, ProductApplyOn, ApplyOn

class ProductListView(View):
    def get(self, request):

        category_id = request.GET.get('category', '1,2').split(',')
        apply_on_id = request.GET.get('apply_on','1,2,3').split(',')
        
        products_in_category = Product.objects.filter(category_id__in=category_id).values_list('id', flat=True)
        products_in_apply_on = ProductApplyOn.objects.filter(apply_on_id__in=apply_on_id).values_list('product_id', flat=True)
        products_in_both     = [id for id in products_in_category if id in products_in_apply_on]
        products             = Product.objects.filter(id__in=products_in_both)

        product_list = [{
            'name' : product.name,
            'price' : product.price,
            'product_id' : product.id,
            'color_id' : product.productimage_set.first().color_id,
            'product_images' : [image_url for image_url in product.productimage_set[:4]]
            } for product in products]
        
        return JsonResponse({"product_list": product_list}, status=200)

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            color_id = request.GET.get('color_id', None)
            
            product = Product.objects.get(id=product_id)

            images         = product.productimage_set.filter(color_id=color_id)
            product_images = [image.image_url for image in images]
            
            if color_id:
                color_ids     = product.productimage_set.values_list('color_id',flat=True).distinct()
                color_options = [{"id": id, "name": Color.objects.get(id=id).name} for id in color_ids]
            else:
                color_options = []
            
            product_info = Product.objects.filter(id = product_id).values()

            product_detail = {
                "product_images" : product_images,     
                "color_options"  : color_options,
                "product_info"   : product_info[0],
            }

            return JsonResponse({"product_detail" : product_detail}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "Product does not exist"}, status=400)

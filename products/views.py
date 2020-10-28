import json

from django.views     import View
from django.http      import HttpResponse, JsonResponse

from products.models import Product, Color, ProductColor, Image, Category, ProductApplyOn, ApplyOn

class ProductListView(View):
    def get(self, request):
        
        category = request.GET.get('category', 'COLOR,CARE').split(',')
        apply_on = request.GET.get('apply_on','LIPS,EYES,FACE').split(',')
        
        category_id = Category.objects.filter(name__in=category).values_list('id',flat=True)
        apply_on_id = ApplyOn.objects.filter(name__in=apply_on).values_list('id',flat=True)

        products_in_category = Product.objects.filter(category_id__in=category_id).values_list('id', flat=True)
        products_in_apply_on = ProductApplyOn.objects.filter(apply_on_id__in=apply_on_id).values_list('product_id', flat=True)
        products_in_both     = [id for id in products_in_category if id in products_in_apply_on]

        products             = Product.objects.filter(id__in=products_in_both)

        product_list = [{
            'name'           : product.name,
            'price'          : product.price,
            'product_id'     : product.id,
            'product_images' : product.productcolor_set.first().image_set.values('product_image', 'model_image')[0], 
            'color_options'  : [{
                'color_id'   : color.color_id,
                'color_name' : color.color.name if color.color_id else ''
                } for color in product.productcolor_set.all()]
            } for product in products]
        
        return JsonResponse({"product_list": product_list}, status=200)

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            
            product_info = Product.objects.filter(id=product_id).values()[0]
            
            product_colors = product.productcolor_set.all()
            
            product_list = [{
                'color_id'  : product.color_id,
                'color_name': product.color.name,
                'images'    : product.image_set.values(
                    'product_image',
                    'model_image',
                    'detail1_image',
                    'detail2_image'
                    )[0]
                } for product in product_colors]

            product_pairs = Product.objects.filter(category_id=product.category_id).exclude(id=product_id)[:2]
            
            pair_with = [{
                "name"       : product.name,
                "price"      : product.price,
                "image"      : product.productcolor_set.first().image_set.values('product_image')[0],
                "product_id" : product.id
                } for product in product_pairs]

            recommendations = Product.objects.all().exclude(id=product_id)

            you_may_also_like = [{
                'name'           : recommendation.name,
                'price'          : recommendation.price,
                'product_id'     : recommendation.id,
                'product_images' : recommendation.productcolor_set.first().image_set.values('product_image', 'model_image')[0],
                } for recommendation in recommendations]

            return JsonResponse({
                "product_info"      : product_info, 
                "product_list"      : product_list,
                "pair_with"         : pair_with,
                "you_may_also_like" : you_may_also_like,
                }, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "Product does not exist"}, status=400)

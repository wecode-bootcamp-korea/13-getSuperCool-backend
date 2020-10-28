import json

from django.views     import View
from django.http      import HttpResponse, JsonResponse

from products.models import Product, Color, ProductColor, Image, Category, ProductApplyOn, ApplyOn

class ProductListView(View):
    def get(self, request):
        products = Product.objects.select_related('category').prefetch_related('productapplyon_set__apply_on','productcolor_set__color')

        product_list = [{
            'name'          : product.name,
            'price'         : product.price,
            'product_id'    : product.id,
            'category'      : product.category.name,
            'apply_on'      : [applyon.apply_on.name for applyon in product.productapplyon_set.all()],
            'product_image' : product.productcolor_set.first().image_set.get().product_image,
            'model_image'   : product.productcolor_set.first().image_set.get().model_image, 
            'colors' : [{
                'color_id'   : color.color_id,
                'color_name' : color.color.name if color.color_id else ''
                } for color in product.productcolor_set.all()]
            } for product in products]
            
        return JsonResponse({"product_list": product_list}, status=200)

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.prefetch_related('productcolor_set__image_set', 'productcolor_set__color').get(id=product_id)

            product_info = [{ 
                'name'         : product.name,
                'description'  : product.description,
                'super_tip'    : product.super_tip,
                'size'         : product.size,
                'good_to_know' : product.good_to_know,
                'contains'     : product.contains,
                'price'        : product.price
                }]
            
            
            color_list = [{
                'color_id'      : product.color_id,
                'color_name'    : product.color.name if product.color_id else "",
                'product_image' : product.image_set.get().product_image,
                'model_image'   : product.image_set.get().model_image,
                'detail1_image' : product.image_set.get().detail1_image,
                'detail2_image' : product.image_set.get().detail2_image
                } for product in product.productcolor_set.all()]

            product_pairs = Product.objects.filter(category_id=product.category_id).exclude(id=product_id)[:2]
            
            pair_with = [{
                "name"          : product.name,
                "price"         : product.price,
                "product_image" : product.productcolor_set.first().image_set.get().product_image,
                "product_id"    : product.id
                } for product in product_pairs]

            recommendations = Product.objects.all().exclude(id=product_id)

            you_may_also_like = [{
                'name'          : recommendation.name,
                'price'         : recommendation.price,
                'product_id'    : recommendation.id,
                'product_image' : recommendation.productcolor_set.first().image_set.get().product_image,
                'model_image'   : recommendation.productcolor_set.first().image_set.get().model_image,
                } for recommendation in recommendations]

            return JsonResponse({
                "product_info"      : product_info, 
                "color_list"        : color_list,
                "pair_with"         : pair_with,
                "you_may_also_like" : you_may_also_like,
                }, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "Product does not exist"}, status=400)

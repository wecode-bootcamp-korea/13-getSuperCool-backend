import json

from django.views import View
from django.http  import HttpResponse, JsonResponse

from products.models import Product, Category, ApplyOn, ProductApplyOn, Color, ProductImage

class ProductListView(View):
    def post(self, request):
        data = json.loads(request.body)

        category = data['category']
        apply_on = data['apply_on']



        return JsonResponse({"product_list": }, status=)



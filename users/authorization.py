import json
import jwt
import my_settings

from django.http import JsonResponse

from .models import User
from products.models import Product

def token_check(func): 
    def wrapper(self, request, *args, **kwargs):

        if "AUTHORIZATION" not in request.headers: 
            return JsonResponse({"message" : "INVALID_LOGIN"}, status=401)

        encode_token = request.headers["AUTHORIZATION"] 

        try:
            user_id = jwt.decode(encode_token, my_settings.SECRET['secret'], algorithm = my_settings.ALGORITHM['algorithm'])                         
            user_filter=User.objects.filter(id=user_id["user_id"])
            if user_filter :
                access_token_id=user_id["user_id"]
            
            else : 
                return JsonResponse({"message":"INVALID_USER"}, status=401)
        except jwt.DecodeError:
            return JsonResponse({"message":"INVALID_TOKEN"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"message":"UNKNOWN_USER"}, status=401)

        return func(self, request,access_token_id,*args ,**kwargs) 

    return wrapper
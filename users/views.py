import json
from django.views import View
from .models      import User
from products.models import Product
from django.http  import JsonResponse
import bcrypt
import jwt
import django
import re
import my_settings

class SignUpView(View):
    def post(self , request):
        try:
            data = json.loads(request.body)
            token =request.headers.get('User-Agent')
            first_name = data["first_name"]
            last_name  = data["last_name"]
            birth_date = data['birth_date']
            email      = data["email"]
            password   = data["password"]

            pattern=r'[A-Z0-9._%+-]+@[A-Z0-9,-]+\.[A-Z]{2,4}'
            regex=re.compile(pattern,flags=re.IGNORECASE)
            
            if len(regex.findall(email)) == 0:
                return JsonResponse({"message":"EMAIL_INVALID"})
            
            if len(password)<8 :
                return JsonResponse({"message": "PASSWORD_LENGTH_ERROR"})

            hash_password   = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
            hash_password_d = hash_password.decode('utf-8')
            User.objects.create(first_name=first_name,last_name=last_name,birth_date=birth_date,email=email,password=hash_password_d)
            return JsonResponse({"message":"SUCCESS"},status=200)

        except django.db.utils.IntegrityError:
            return JsonResponse({"message":"DUPLICATE"})

        except KeyError : 
            return JsonResponse({"message":"KEY_ERROR"})

class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)
        
        email      = data["email"]
        password   = data["password"]
        
        get_email= User.objects.get(email=email).id
        get_pw_s=User.objects.get(email=email).password
        get_pw_b=get_pw_s.encode('utf-8')
            
        if bcrypt.checkpw(password.encode('utf-8'), get_pw_b) :
            access_token    = jwt.encode({'user_id' : get_email}, my_settings.SECRET['secret'], algorithm = 'HS256') 
            token=access_token.decode('utf-8') 
            return JsonResponse ({"message":"SUCCESS",'Authorization':token } )
                
        else :
            return JsonResponse({"message":"INVALID EMAIL OR PASSWORD"})
        


     



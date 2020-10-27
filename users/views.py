import bcrypt
import jwt
import re
import my_settings
import json

import django
from django.views import View
from django.http  import JsonResponse

from .models      import User

class SignUpView(View):
    def post(self , request):
        try:
            data = json.loads(request.body)

            first_name = data["first_name"]
            last_name  = data["last_name"]
            birth_date = data['birth_date']
            email      = data["email"]
            password   = data["password"]

            pattern=r'[A-Z0-9._%+-]+@[A-Z0-9,-]+\.[A-Z]{2,4}'
            regex  = re.compile(pattern,flags=re.IGNORECASE)
            
            if len(regex.findall(email)) == 0:
                return JsonResponse({"message":"EMAIL_INVALID"},status=400)
            
            if len(password)<8 :
                return JsonResponse({"message": "PASSWORD_TOO_SHORT"},status=400)

            hash_password   = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
           
            User.objects.create(
                first_name  =first_name,
                last_name   =last_name,
                birth_date  =birth_date,
                email       =email,
                password    =hash_password
                )

            return JsonResponse({"message":"SUCCESS"},status=200)

        except django.db.utils.IntegrityError:
            return JsonResponse({"message":"DUPLICATE"},status=400)

        except KeyError : 
            return JsonResponse({"message":"KEY_ERROR"},status=400)

class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)
        
        email     = data["email"]
        password  = data["password"]
        
        get_email = User.objects.filter(email=email)

        if get_email :
           
            get_pw  = User.objects.get(email=email).password.encode('utf-8')

            if bcrypt.checkpw(password.encode('utf-8'), get_pw) :
                access_token    = jwt.encode({'user_id' : get_email[0].id}, my_settings.SECRET['secret'], algorithm = my_settings.ALGORITHM['algorithm']).decode('utf-8') 
                return JsonResponse ({"message":"SUCCESS",'Authorization':access_token } )
                    
            else :
                return JsonResponse({"message":"INVALID EMAIL OR PASSWORD"},status=400)
        else :
            return JsonResponse({"message":"INVALID EMAIL OR PASSWORD"},status=400)
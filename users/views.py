import json
from django.views import View
from .models      import User
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

            first_name = data["first_name"]
            last_name  = data["last_name"]
            birth_date = data['birth_date']
            email      = data["email"]
            password   = data["password"]

            pattern=r'[A-Z0-9._%+-]+@[A-Z0-9,-]+\.[A-Z]{2,4}'
            regex=re.compile(pattern,flags=re.IGNORECASE)
            
            if len(regex.findall(email)) == 0:
                return JsonResponse({"Message":"EMAIL_NOT_VALID"})

            hash_password   = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
            hash_password_d = hash_password.decode('utf-8')
            User.objects.create(first_name=first_name,last_name=last_name,birth_date=birth_date,email=email,password=hash_password_d)
            return JsonResponse({"Message":"SUCCESS"},status=200)

        except django.db.utils.IntegrityError:
            return JsonResponse({"Message":"DUPLICATE"})

        except KeyError : 
            return JsonResponse({"Message":"KEY_ERROR"})


class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)
        
        email      = data["email"]
        password   = data["password"]
        
        get_email= User.objects.get(email=email).id
        get_pw_s=User.objects.get(email=email).password
        get_pw_b=get_pw_s.encode('utf-8')
            
        if bcrypt.checkpw(password.encode('utf-8'), get_pw_b) :
            access_token    = jwt.encode({'user_id' : get_email}, my_settings.SECRET['secret'], algorithm = 'HS256') #토큰변환 (유저 이메일에서 id값을찾아변환)
            # access_token_d  = jwt.decode(access_token ,my_settings.SECRET['secret'], algorithm = 'HS256') #((유저 이메일에서 id값을찾아변환)한걸 Decoding)
            # acress_token_id = access_token_d["user_id"]  # 토큰 문자열 변환한걸 acress_token_id 대입
            token=access_token.decode('utf-8') 
            return JsonResponse ({"Message":"SUCCESS",'token':token})
                
        else :
            return JsonResponse({"Message":"NOT VALIED EMAIL OR PW"})
        

class InquiriesView(View):
    pass

class ForgotPasswordView(View):
    pass

class DiscountView(View):
    def post(self,request):
        data=json.loads(request.body)
        
        email=data["email"]
import json
from django.views import View
from .models      import User
from django.http  import JsonResponse
import bcrypt
import jwt
import django
import re
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
        
        # data = json.loads(request.body)
        
        # email      = data["email"]
        # password   = data["password"]
        
        # return JsonResponse({"Message":"SUCCESS"})
        # get_pw_s=User.objects.get(email=email).password
        # get_pw_b=get_pw_s.encode('utf-8')

        # if bcrypt.checkpw(password.encode('utf-8'), get_pw_b) :
        #     return({"Message":"SUCCESS"})



        

            
            


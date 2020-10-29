import bcrypt
import jwt
import re
import my_settings
import json
import random
import string

import django
from django.views import View
from django.http  import JsonResponse

from .models         import User,Like,Subscription,Inquiry,Subject
from orders.models   import Order
from products.models import Product
from  .authorization     import token_check

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

            return JsonResponse({"message":"SUCCESS"},status=201)

        except django.db.utils.IntegrityError:
            return JsonResponse({"message":"DUPLICATE"},status=400)

        except KeyError : 
            return JsonResponse({"message":"KEY_ERROR"},status=400)

class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)
        
        email      = data["email"]
        password   = data["password"]
        
        users = User.objects.filter(email=email)

        if users :
           
            get_pw  = User.objects.get(email=email).password.encode('utf-8')

            if bcrypt.checkpw(password.encode('utf-8'), get_pw) :
                access_token    = jwt.encode({'user_id' : users[0].id}, my_settings.SECRET['secret'], algorithm = my_settings.ALGORITHM['algorithm']).decode('utf-8')
                
                return JsonResponse ({"message":"SUCCESS",'AUTHORIZATION':access_token },status=201)
                    
            else :
                return JsonResponse({"message":"INVALID EMAIL OR PASSWORD"},status=400)
        else :
            return JsonResponse({"message":"INVALID EMAIL OR PASSWORD"},status=400)
            
class InquiriesView(View):
    def post(self,request) :
        data  = json.loads(request.body)

        email   = data["email"]
        name    = data["name"]
        order   = data["order"]
        country = data["country"]
        subject = data["subject"]
        message = data["message"]

        subjects=Subject.objects.get(id=subject).id
        
        Inquiry.objects.create(
            email=email,
            name=name,
            country=country,
            message=message,
            order_id=order,
            subject_id=subjects,
            )
        return JsonResponse({"message":"SUCCESS"},status=201)

class ForgotPasswordView(View):
    def post(self,request) :
        data  = json.loads(request.body)
        
        email = data["email"]
        users = User.objects.filter(email=email)

        STRING_LENGTH = 10 
        string_pool   = string.ascii_lowercase 

        if users : 
            new_pw = "" 
            for i in range(STRING_LENGTH) :
                new_pw += random.choice(string_pool)

            new_pw_decode = bcrypt.hashpw(result.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            User.objects.filter(email=email).update(password=new_pw_decode)
            return JsonResponse({"message":"SUCCESS",'new_pw':new_pw},status=201)
      
        else : 
            return JsonResponse({"message":"EMAIL_NOT_EXIST"},status=400)

class DiscountView(View):
    def post(self,request):

        data=json.loads(request.body)

        email=data["email"]

        pattern =r'[A-Z0-9._%+-]+@[A-Z0-9,-]+\.[A-Z]{2,4}'
        regex   =re.compile(pattern,flags=re.IGNORECASE)   
             
        get_email = Subscription.objects.filter(email=email)

        if len(regex.findall(email)) == 0:
            return JsonResponse({"message":"EMAIL_INVALID"},status=400)
        
        elif len(get_email) ==  0 :
            Subscription.objects.create(email=email)
            return JsonResponse({"discount_code" : "SUPERCOOL20"},status=200)
        else :
            return JsonResponse({"message":"EMAIL_DUPLICATE"},status=400)

class LikeView(View):
    @token_check
    def post(self , request,access_token_id):
        try:    
            data = json.loads(request.body)

            product_id = data["product_id"]

            get_user_id    = User.objects.filter(id=access_token_id)[0].id
            get_product_id = Product.objects.filter(id=product_id)[0].id
            
            if get_user_id and get_product_id :
                Like.objects.create(user_id = get_user_id , product_id=get_product_id)
                return JsonResponse({"message":access_token_id},status=201)
            
            else : 
                return JsonResponse({"message":"user_id or product_id INVALID"},status=401)
        
        except IndexError:
            return JsonResponse({"message":"user_id or product_id INVALID"},status=401)
            
        
       
        




        
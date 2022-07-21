import json

import re
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse
from django.core.exceptions import ValidationError
from django.conf  import settings

from user.models import StoreUser
from user.validation import signup_user_name, signup_email, signup_password

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            user_name    = data['user_name']
            password     = data['password']
            name         = data['name']
            phone_number = data['phone_number']
            email        = data['email']

            # REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            # REGEX_PASSWORD = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*()])[A-Za-z\d~!@#$%^&*()]{8,16}'
            # REGEX_USER_NAME = '^[a-zA-Z0-9]{4,16}$'

            # if not re.match(REGEX_USER_NAME, user_name):
            #     return JsonResponse({'message':'INVALID_ID_FORMET'}, status=400) 

            # if not re.match(REGEX_PASSWORD, password):
            #     return JsonResponse({'message':'INVALID_PASSWORD_FORMET'}, status=400)            

            # if not re.match(REGEX_EMAIL, email):
            #     return JsonResponse({'message':'INVALID_EMAIL_FORMET'}, status=400)

            signup_user_name(user_name)

            signup_email(email)

            signup_password(password)

            if StoreUser.objects.filter(user_name=user_name).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=400) 

            hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            StoreUser.objects.create(
                user_name    = user_name,
                password     = hash_password,
                name         = name,
                phone_number = phone_number,
                email        = email,
            )
            return JsonResponse({'massage':'SUCCESS'}, status=201)
        
        except ValidationError as error:
            return JsonResponse({"message" : error.message}, status = 400)

        except json.JSONDecodeError:
            return JsonResponse({'message':'JSONDecodeError'}, status=400)           

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            user_name = data['user_name']
            password  = data['password']

            user = StoreUser.objects.get(user_name=user_name)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_USER'}, status=401)
        
            access_token = jwt.encode({'id': user.id}, settings.SECRET_KEY, settings.ALGORITHM)

            return JsonResponse({'massage':access_token}, status=200)

        except StoreUser.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)        



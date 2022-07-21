import json

import re
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse
from django.conf  import settings

from users.models import User

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            user_name     = data['user_name']
            password      = data['password']
            name          = data['name']
            mobile_number = data['mobile_number']
            email         = data['email']

            REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            REGEX_PASSWORD = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*()])[A-Za-z\d~!@#$%^&*()]{8,16}'

            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({'message':'INVALID_EMAIL_FORMET'}, status=400)

            # 최대 8~16자리 영문 대문자,소문자,특수문자(~!@#$%^&*()_-+
            if not re.match(REGEX_PASSWORD, password):
                return JsonResponse({'message':'INVALID_PASSWORD_FORMET'}, status=400)

            if User.objects.filter(user_name=user_name).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=400) 

            hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                user_name     = user_name,
                password      = hash_password,
                name          = name,
                mobile_number = mobile_number,
                email         = email,
            )
            return JsonResponse({'massage':'SUCCESS'}, status=201)

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

            user = User.objects.get(user_name=user_name)

            if not bcrypt.checkpw(password.encode('uft-8'), user.password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_USER'}, status=401)
        
            access_token = jwt.encode({'id': user.id}, settings.SECRET_KEY, ALGORITHM=settings.ALGORITHM)

            return JsonResponse({'massage':access_token}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)        






from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

from .serializers import RegisterSerializer 

User=get_user_model()


class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self,request):
        data=request.data
        serializer=RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print(serializer)
            serializer.save()
        return Response('Вы успешно зарегистрировались',201)
    
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response('Пользователь успешно удален',204)
    
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = RegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=404)

    def patch(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = RegisterSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    



class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('Пользователь не найден', 404)
        user.activation_code = ''
        user.is_active = True 
        user.save()
        return Response('Вы успешно активировали аккаунт', 200)
    




import datetime
import logging
import requests
from environs import Env
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from django.db.models import Q
import requests
from environs import Env
import logging
from django.contrib.auth.models import User
from .serializer import UserSerializer,ComplaintSerializer,OrganSerializer
from web_interface.models import Complaint,Organ

class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["GET"], name="Get All Telegram Users")
    def all(self, request):
        """Get all TelegramUsers"""
        users = User.objects.all()
        return Response(users)
    
    @action(detail=False, methods=["POST"], name="Create Telegram User", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication]) 
    def createUser(self, request):
        """Create a TelegramUser"""
        telegram_user = TelegramUser.objects.create(
            chat_id=request.data['chat_id'],
            name=request.data['name'],
            nick_name = request.data['nick_name'],
            date_join=request.data['date_join'])
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], name="Get one Telegram User", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication])
    def getUser(self, request, pk=None):
        """Get one TelegramUser"""
        telegram_user = get_object_or_404(TelegramUser, chat_id=pk)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)
    
    
    @action(detail=True, methods=["GET"], name="Get one Telegram User by ID in model", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication])
    def getUserById(self, request, pk=None):
        """Get one TelegramUser by ID in model"""
        telegram_user = get_object_or_404(TelegramUser, id=pk)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)
    
    @action(detail=True, methods=["GET"], name="Get user balance", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication]) 
    def getUserBalance(self, request,pk=None):
        """Get user balance"""
        balance = get_object_or_404(TelegramUser, chat_id=pk).balance
        return Response(balance)
    
class OrgansView(viewsets.ModelViewSet):
    queryset = Organ.objects.all()
    serializer_class = OrganSerializer

    @action(detail=False, methods=["GET"], name="Get All Telegram Users")
    def all(self, request):
        """Get all TelegramUsers"""
        users = User.objects.all()
        return Response(users)
    
    @action(detail=False, methods=["POST"], name="Create Telegram User", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication]) 
    def createUser(self, request):
        """Create a TelegramUser"""
        telegram_user = TelegramUser.objects.create(
            chat_id=request.data['chat_id'],
            name=request.data['name'],
            nick_name = request.data['nick_name'],
            date_join=request.data['date_join'])
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], name="Get one Telegram User", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication])
    def getUser(self, request, pk=None):
        """Get one TelegramUser"""
        telegram_user = get_object_or_404(TelegramUser, chat_id=pk)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)
    
    
    @action(detail=True, methods=["GET"], name="Get one Telegram User by ID in model", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication])
    def getUserById(self, request, pk=None):
        """Get one TelegramUser by ID in model"""
        telegram_user = get_object_or_404(TelegramUser, id=pk)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)
    
    @action(detail=True, methods=["GET"], name="Get user balance", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication]) 
    def getUserBalance(self, request,pk=None):
        """Get user balance"""
        balance = get_object_or_404(TelegramUser, chat_id=pk).balance
        return Response(balance)
    
class ComplaintsView(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    @action(detail=False, methods=["GET"], name="Get All Telegram Users")
    def all(self, request):
        """Get all TelegramUsers"""
        users = User.objects.all()
        return Response(users)
    
    @action(detail=False, methods=["POST"], name="Create Telegram User", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication]) 
    def createUser(self, request):
        """Create a TelegramUser"""
        telegram_user = TelegramUser.objects.create(
            chat_id=request.data['chat_id'],
            name=request.data['name'],
            nick_name = request.data['nick_name'],
            date_join=request.data['date_join'])
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], name="Get one Telegram User", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication])
    def getUser(self, request, pk=None):
        """Get one TelegramUser"""
        telegram_user = get_object_or_404(TelegramUser, chat_id=pk)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)
    
    
    @action(detail=True, methods=["GET"], name="Get one Telegram User by ID in model", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication])
    def getUserById(self, request, pk=None):
        """Get one TelegramUser by ID in model"""
        telegram_user = get_object_or_404(TelegramUser, id=pk)
        serializer = TelegramUserSerializer(telegram_user)
        return Response(serializer.data)
    
    @action(detail=True, methods=["GET"], name="Get user balance", 
            permission_classes = [IsAuthenticated], 
            authentication_classes = [SessionAuthentication, TokenAuthentication]) 
    def getUserBalance(self, request,pk=None):
        """Get user balance"""
        balance = get_object_or_404(TelegramUser, chat_id=pk).balance
        return Response(balance)
    

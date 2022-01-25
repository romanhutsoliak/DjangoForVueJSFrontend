from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from .models import Account, CurrencyRates, Category, AccountHistory
from .serializers import AccountSerializer, CurrencyRatesSerializer, CategorySerializer, AccountHistoryListSerializer, AccountHistoryCreateSerializer, PlanningSerializer
from rest_framework import viewsets, generics, permissions
import requests, json
from rest_framework.views import APIView
from django.db.models import Sum, Count
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AccountView(request, *args, **kwargs):

    try:
        account = Account.objects.get(user_id=request.user.id)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def CurrencyRatesView(request, *args, **kwargs):
    try:
        currencyRates = CurrencyRates.objects.get(id=1)
    except CurrencyRates.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CurrencyRatesSerializer(currencyRates)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class AccountHistoryViewSet(viewsets.ModelViewSet):
    queryset = AccountHistory.objects.all()
    permission_classes = [IsAuthenticated]
    #PageNumberPagination.page_size = 2 

    def perform_create(self, serializer):
        try:
            account = Account.objects.get(user_id=serializer.context['request'].user.id)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if serializer.validated_data['type'] == 1:
            account.amount = account.amount + int(serializer.validated_data['amount'])
        else:
            account.amount = account.amount - int(serializer.validated_data['amount'])
        account.save()

        serializer.save()

    def get_serializer_class(self):
        if self.action == 'list' or  self.action == 'retrieve':
            return AccountHistoryListSerializer
        elif self.action == "create" or  self.action == "update":
            return AccountHistoryCreateSerializer


class PlanningView(generics.ListAPIView):
    serializer_class = PlanningSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        categories = Category.objects.all().prefetch_related('history').annotate(category_amount_spend=Sum('history__amount'))
        return categories
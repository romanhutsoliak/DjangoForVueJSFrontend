from .models import *
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from datetime import datetime

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('amount', 'user')

class CurrencyRatesSerializer(ModelSerializer):
    EUR_formated = serializers.SerializerMethodField()
    USD_formated = serializers.SerializerMethodField()

    def get_EUR_formated(self, obj):
        return "{:.2f}".format(obj.EUR)

    def get_USD_formated(self, obj):
        return "{:.2f}".format(obj.USD)

    class Meta:
        model = CurrencyRates
        fields = ('RUB', 'EUR', 'USD', 'date', 'EUR_formated', 'USD_formated')

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'limit')
        read_only_fields = ('id',)

class AccountHistoryListSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = AccountHistory
        # depth = 1
        fields = ('id', 'amount', 'category_id', 'type', 'description', 'category')
        read_only_fields = ('id',)

class AccountHistoryCreateSerializer(ModelSerializer):
    class Meta:
        model = AccountHistory
        fields = "__all__"
        #fields = ('id', 'amount', 'category_id', 'type', 'description', 'category')
        read_only_fields = ('id',)

    def validate_amount(self, value):
        try:
            account = Account.objects.get(user_id=self.context['request'].user.id)
        except Account.DoesNotExist:
            raise serializers.ValidationError("account")

        if self.context['request'].data['type'] == '0' and account.amount < value:
            raise serializers.ValidationError("Account has not enough money")

        return value;

    def validate(self, data):
        try:
            account = Account.objects.get(user_id=self.context['request'].user.id)
        except Account.DoesNotExist:
            raise serializers.ValidationError("Account does not exist")

        #other wise you can set default value of age here,
        if data.get('account', None) == None: #this conditon will be true only when age = serializer.IntergerField(required=False)
            data['account'] = account
        return data


class PlanningHistorySerializer(ModelSerializer):
    class Meta:
        model = AccountHistory
        fields = ('amount', 'type')

class PlanningSerializer(ModelSerializer):
    # histories = PlanningHistorySerializer(source='history', read_only=True, many=True)
    category_amount_spend = serializers.CharField(default=0)
    class Meta:
        model = Category
        # fields = ('id', 'name', 'limit', 'category_amount_spend') #, 'history_history_spend_amount'
        fields = "__all__"
        

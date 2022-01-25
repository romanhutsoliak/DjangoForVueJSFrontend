from django.urls import path, include
from apiapp import views
from rest_framework import routers

urlpatterns = [
    path('current-user/account/', views.AccountView),
    path('currency-rates/', views.CurrencyRatesView),
    path('categories/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('account-histories/<int:pk>/', views.AccountHistoryViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('account-histories/', views.AccountHistoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('planning/', views.PlanningView.as_view()),
]
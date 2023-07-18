from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (ProdutoCreateAPIView, ProdutoDeleteAPIView,
                    ProdutoListAPIView, ProdutoUpdateAPIView, ProdutoViewSet, vender_produto)

app_name="api"

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)


urlpatterns = [
    path('produtos/', ProdutoListAPIView.as_view(), name='produto-list'),
    path('produtos/create/', ProdutoCreateAPIView.as_view(), name='produto-create'),
    path('produtos/update/<int:pk>/', ProdutoUpdateAPIView.as_view(), name='produto-update'),
    path('produtos/delete/<int:pk>/', ProdutoDeleteAPIView.as_view(), name='produto-delete'),
    path('produtos/<int:pk>/vender/<int:qtd>/', vender_produto, name='vender_produto'),
] + router.urls

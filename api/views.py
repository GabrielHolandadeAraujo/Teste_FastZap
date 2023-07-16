import logging

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Produto
from .serializers import ProdutoSerializer


#Todas
class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    logging.info('Listagem de produtos realizada com sucesso')



#Create
class ProdutoCreateAPIView(APIView):
    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logging.info('Criação de produtos realizada com sucesso')
            return Response(serializer.data, status=status.HTTP_201_CREATED)            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Read
class ProdutoListAPIView(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        logging.info('Listagem de produtos realizada com sucesso')
        return Response(serializer.data)


#Update
class ProdutoUpdateAPIView(APIView):
    def put(self, request, pk):
        produto = Produto.objects.get(pk=pk)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data)
        logging.info('Update de produtos realizada com sucesso')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Delete
class ProdutoDeleteAPIView(APIView):
    def delete(self, request, pk):
        produto = Produto.objects.get(pk=pk)
        produto.delete()
        logging.info('Delete de produtos realizada com sucesso')
        return Response(status=status.HTTP_204_NO_CONTENT)



#Função de Venda
def vender_produto(request, pk, qtd):
    produto = get_object_or_404(Produto, pk=pk)
    
    # Realize a ação de venda aqui, como atualizar a quantidade em estoque
    if(produto.quantidade>0 and qtd>0 and produto.quantidade>=qtd):
        produto.quantidade -= qtd
       
        # Exiba os dados do produto no terminal
        print("Produto vendido:")
        print("Nome:", produto.nome)
        print("Descrição:", produto.descricao)
        print("Preço:", produto.preco)
        print("Quantidade em estoque:", produto.quantidade)

        logging.info('Venda de produtos realizada com sucesso. Produto vendido: %s. Quantidade em estoque: %s', produto.nome, produto.quantidade)

        produto.save()
      

        #Mensagem de retorno Json    
        return JsonResponse({'message': 'Venda Realizada Com Sucesso.'})
    else:
        logging.info('Venda de produtos Nao Foi realizada com sucesso, Produto nao possui Estoque.')
        return JsonResponse({'message': 'Produto sem estoque Suficiente, nao foi possivel realizar a Venda.'})
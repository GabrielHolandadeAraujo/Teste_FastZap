import logging
import time

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from FastZapTest.celery import app

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
        try:
            produto = Produto.objects.get(pk=pk)
        except:
            raise ValidationError
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data)
        logging.info('Update de produtos realizada com sucesso')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Delete
class ProdutoDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            produto = Produto.objects.get(pk=pk)
        except:
            raise ValidationError
        produto.delete()
        logging.info('Delete de produtos realizada com sucesso')
        return Response(status=status.HTTP_204_NO_CONTENT)



#Função de Venda
def vender_produto(request, pk, qtd):
    try:
        produto = Produto.objects.get(pk=pk)
    except:
        raise ValidationError
    mandarEmail.apply_async(args=[pk])
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
        return JsonResponse({'message': 'Venda realizada com sucesso.'})
    elif (qtd<=0):
        logging.info('Venda de produtos nao foi realizada com sucesso, quantidade querida menor que 1.')
        return JsonResponse({'message': 'quantidade requerida menor que 1, nao foi possivel realizar a Venda.'})
    else:    
        logging.info('Venda de produtos nao foi realizada com sucesso, Produto nao possui Estoque.')
        return JsonResponse({'message': 'Produto sem estoque suficiente, nao foi possivel realizar a Venda.'})

@app.task(bind=True)    
def mandarEmail(task_definition, produto_pk):
    time.sleep(5)
    print(f"Um e-mail foi enviado para o produto de ID {produto_pk}")
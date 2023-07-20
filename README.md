
# Teste FastZap


### Preparando o ambiente

```
sudo apt-get install python3-venv
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
```

#### Clonando o repositório

```
git clone your-url.git
```

### Executar o container

```
docker-compose build (se não funcionar adicione sudo no inicio do comando)
```

### Subir a imagem para o Docker

```
docker-compose up -d (se não funcionar adicione sudo no inicio do comando)
```

## Informações de uso

####  Rota principal

```
  'localhost:8000/produtos/'
```

####  Formato json para criar produtos

```
  Exemplo:
  
  {
  "nome": "Novo nome do produto",
  "descricao": "Nova descrição do produto",
  "preco": 29.99
  "quantidade": 3
}
```

#### Para realizar vendas

```
  O formato da rota de venda é: "localhost:8000/produtos/<id do produto>/vender/<quantidade de produtos que serão vendidos>/'
```




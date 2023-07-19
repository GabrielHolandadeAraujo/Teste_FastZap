
# Teste FastZap

## 1 - Para executar dentro do docker

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

## 2- Para executar fora do docker

### Preparando o ambiente

```
sudo apt-get install python3-venv
```

#### criando o ambiente virtual

```
python3 -m venv venv
```

#### Clonando o repositório

```
git clone your-url.git
```

#### Instalando os requisitos

```
 pip install -r requirements.txt
```

#### Criando a base de dados

```
python manage.py migrate
```

#### Criando um super usuário

```
python manage.py createsuperuser
```

#### Executar projeto

```
  python manage.py runserver
```

## 3 - Informações de uso

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
  O formato da rota de venda é: "produtos/<id do produto>/vender/<quantidade de produtos que serão vendidos>/'
```




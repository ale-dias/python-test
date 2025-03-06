# Análise e Recomendação de Filmes

Este projeto contém dois scripts em Python para análise de filmes usando a API do **The Movie Database (TMDb)**.

## 📌 Estrutura do Projeto

- `teste_1.py` – Analisa dados de filmes, frequência de gênero, incluindo atores e bilheteria.
- `teste_2.py` – Retorna recomendações de filmes baseadas em um filme fornecido.
- `README.md` – Explicação de como rodar os scripts.

## 🚀 Como Configurar e Rodar os Scripts

### 1️⃣ Pré-requisitos
- Python 3 instalado
- Biblioteca `requests` instalada
- Chave de API do TMDb

### 2️⃣ Instalar Dependências
Se ainda não tiver a biblioteca `requests`, instale com:
```sh
pip install requests
```

### 3️⃣ Configurar a Chave da API
- Substitua `SUA_API_AQUI` nos scripts pela sua chave de API do TMDb.

### 4️⃣ Executar os Scripts
Para rodar os scripts, use:
```sh
python teste_1.py
```
```sh
python teste_2.py
```

## 📊 Saída Esperada

### Exemplo de saída do `teste_1.py`:
```
### Análise dos Filmes ###
Ator: Robert Downey Jr. - 5 filmes
Ator: Scarlett Johansson - 4 filmes
...
Frequência de Gêneros
Drama: 4 vez(es)
Crime: 3 vez(es)
Thriller: 2 vez(es)
...
Top 5 Atores com Maior Bilheteria:
1. Robert Downey Jr. - $3.2 bilhões
...
```

### Exemplo de saída do `teste_2.py`:
```
### Filmes Recomendados ###
Harry Potter e a Câmara Secreta (2002)
Harry Potter e o Prisioneiro de Azkaban (2004)
...
```



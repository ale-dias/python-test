import requests  # Importamos a biblioteca requests para fazer chamadas HTTP
import json  # Importamos json para formatar a saída dos dados

# Chave de API do TMDb (substitua pela sua chave válida)
API_KEY = "fa51e2e027f968ba6fd5386dc6649d6a"
BASE_URL = "https://api.themoviedb.org/3"

# Função para buscar detalhes de um filme pela API
def buscar_detalhes_filme(filme_id):
    url = f"{BASE_URL}/movie/{filme_id}?api_key={API_KEY}&language=pt-BR&append_to_response=credits"
    resposta = requests.get(url)  # Faz a requisição HTTP
    if resposta.status_code == 200:
        return resposta.json()  # Retorna os dados em formato JSON
    else:
        print(f"Erro ao buscar filme {filme_id}: {resposta.status_code}")
        return None

# Lista de filmes de exemplo (IDs do TMDb)
lista_filmes = [550, 278, 680, 155, 13]  # Exemplo com 5 filmes

# Dicionários para armazenar os dados
atores_participacao = {}  # Guarda quantos filmes cada ator participou
generos_frequencia = {}  # Guarda a contagem de cada gênero
atores_bilheteria = {}  # Guarda a soma da bilheteria de cada ator

# Processa cada filme da lista
for filme_id in lista_filmes:
    filme = buscar_detalhes_filme(filme_id)
    if filme:
        # Contabiliza os gêneros do filme
        for genero in filme["genres"]:
            nome_genero = genero["name"]
            generos_frequencia[nome_genero] = generos_frequencia.get(nome_genero, 0) + 1

        # Contabiliza os atores e bilheteria
        for ator in filme["credits"]["cast"][:10]:  # Pegamos apenas os 10 primeiros atores
            nome_ator = ator["name"]
            atores_participacao[nome_ator] = atores_participacao.get(nome_ator, 0) + 1
            atores_bilheteria[nome_ator] = atores_bilheteria.get(nome_ator, 0) + filme.get("revenue", 0)

# Ordena os 5 atores com maior bilheteria
top_5_atores = sorted(atores_bilheteria.items(), key=lambda x: x[1], reverse=True)[:5]

# Exibe os resultados formatados
print("\n### Participação por Ator ###")
for ator, qtd in atores_participacao.items():
    print(f"{ator}: {qtd} filme(s)")

print("\n### Frequência de Gêneros ###")
for genero, qtd in generos_frequencia.items():
    print(f"{genero}: {qtd} vez(es)")

print("\n### Top 5 Atores com Maior Bilheteria ###")
for ator, bilheteria in top_5_atores:
    print(f"{ator}: ${bilheteria:,}")

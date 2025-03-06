import requests  # Biblioteca para fazer requisições HTTP

# Chave da API do TMDb 
API_KEY = "fa51e2e027f968ba6fd5386dc6649d6a"
BASE_URL = "https://api.themoviedb.org/3"

# Função para obter recomendações de filmes
def recomendar_filmes(filme_id):
    url = f"{BASE_URL}/movie/{filme_id}/recommendations?api_key={API_KEY}&language=pt-BR"
    resposta = requests.get(url)  # Faz a requisição para a API
    if resposta.status_code == 200:
        dados = resposta.json()
        recomendacoes = dados.get("results", [])  # Obtém a lista de filmes recomendados
        return recomendacoes[:5]  # Retorna apenas os 5 primeiros
    else:
        print(f"Erro ao buscar recomendações para o filme {filme_id}: {resposta.status_code}")
        return []

# ID do primeiro filme de Harry Potter no TMDb
id_harry_potter = 671  # Harry Potter e a Pedra Filosofal

# Busca recomendações
recomendacoes = recomendar_filmes(id_harry_potter)

# Exibe as recomendações
print("\n### Filmes Recomendados ###")
for filme in recomendacoes:
    print(f"{filme['title']} ({filme['release_date'][:4]})")

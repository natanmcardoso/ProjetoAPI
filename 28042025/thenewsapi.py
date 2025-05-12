# Importa o módulo 'requests' para fazer requisições HTTP
import requests

# Importa o módulo 'os' para acessar variáveis de ambiente do sistema
import os

# Importa a função 'load_dotenv' da biblioteca 'dotenv' para carregar variáveis do arquivo .env
from dotenv import load_dotenv

# Carrega as variáveis de ambiente definidas no arquivo .env
load_dotenv()

# Obtém a chave da API (NEWS_API_KEY) das variáveis de ambiente
api_key = os.getenv('NEWS_API_KEY')

# Define a URL do endpoint da NewsAPI (rota /v2/everything), que retorna resultados de busca de notícias
url = "https://newsapi.org/v2/everything"

# Define os cabeçalhos da requisição, incluindo a chave da API no campo 'x-api-key'
headers = {
    'x-api-key': api_key
}

# Define os parâmetros da requisição:
# 'q' é o termo de busca (notícias contendo "Python")
# 'language' é o idioma dos resultados ('pt' para português)
# 'page' indica que estamos pedindo a segunda página de resultados
params = {
    'q': 'Python',
    'language': 'pt',
    'page': '2'
}

# Realiza uma requisição GET para a API, passando cabeçalhos e parâmetros
resposta = requests.get(url, headers=headers, params=params)

# Exibe o código de status da resposta (200 = sucesso, 401 = não autorizado, etc.)
print(resposta.status_code)

# Converte a resposta da API para um dicionário Python (formato JSON)
resposta_json = resposta.json()

# Exibe o conteúdo da resposta (em JSON) no terminal
print(resposta_json)

# Exibe o nome da fonte da oitava notícia retornada
print(resposta_json['articles'][7]['source']['name'])

# Itera sobre os 10 primeiros artigos retornados e imprime título, descrição e link
for artigo in resposta_json['articles'][:10]:
    print('\n')  # Linha em branco para separar visualmente cada notícia
    print(artigo['title'])         # Título da notícia
    print(artigo['description'])   # Descrição da notícia
    print(artigo['url'])           # URL da notícia

# Verifica se a chave da API foi carregada corretamente
# OBS: este trecho deveria estar acima da requisição, idealmente
if not api_key:
    raise ValueError('API Key não foi localizada nas variáveis de ambiente.')

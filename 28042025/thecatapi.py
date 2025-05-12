# Importa as bibliotecas necessárias
import requests            # Usada para fazer requisições HTTP
import os                  # Usada para acessar variáveis de ambiente do sistema
import webbrowser          # Usada para abrir links no navegador
from dotenv import load_dotenv  # Usada para carregar variáveis de ambiente de um arquivo .env

# Carrega as variáveis do arquivo .env para o ambiente do sistema
load_dotenv()

# Lê a variável de ambiente com a chave da API do TheCatAPI
API_KEY = os.getenv('CAT_API_KEY')

# Verifica se a chave da API foi carregada corretamente
if not API_KEY:
    raise ValueError("A variável CAT_API_KEY não foi encontrada. Verifique o arquivo .env!")

# Define a URL do endpoint da API que retorna imagens de gatos
url = 'https://api.thecatapi.com/v1/images/search'

# Define os cabeçalhos da requisição, incluindo a chave da API
headers = {
    'x-api-key': API_KEY
}

# Realiza uma requisição GET à API
response = requests.get(url, headers=headers)

# Verifica se a resposta foi bem-sucedida (status 200)
if response.status_code == 200:
    # Converte a resposta JSON em um dicionário Python
    data = response.json()
    
    # Verifica se há dados na resposta
    if data:
        # Extrai a URL da imagem do primeiro item retornado
        image_url = data[0]['url']
        print("Imagem encontrada:")
        print(image_url)
        
        # Abre a imagem no navegador padrão do usuário
        webbrowser.open(image_url)
        
        # Verifica se há informações de raça incluídas na imagem
        if 'breeds' in data[0] and data[0]['breeds']:
            # Extrai o primeiro item da lista de raças
            breed_info = data[0]['breeds'][0]
            
            # Coleta as informações da raça com tratamento de campos opcionais
            breed_name = breed_info.get('name', 'Desconhecida')
            breed_weight = breed_info.get('weight', {})
            breed_temperament = breed_info.get('temperament', 'Sem temperamento disponível.')
            breed_origin = breed_info.get('origin', 'Origem desconhecida.')
            breed_lifespan = breed_info.get('life_span', 'Desconhecida')
            breed_wikipedia = breed_info.get('wikipedia_url', 'Sem link disponível.')
            
            # Exibe as informações da raça no terminal
            print(f"\nInformações sobre a raça {breed_name}:")
            print(f"  Peso: {breed_weight.get('imperial', 'Desconhecido')} (imperial) / {breed_weight.get('metric', 'Desconhecido')} (métrico)")
            print(f"  Temperamento: {breed_temperament}")
            print(f"  Origem: {breed_origin}")
            print(f"  Expectativa de vida: {breed_lifespan} anos")
            print(f"  Link do Wikipedia: {breed_wikipedia}")
        else:
            # Caso não haja informações de raça
            print("Informações de raça não disponíveis.")
    
    else:
        # Caso a resposta não contenha dados válidos
        print("Nenhuma imagem encontrada.")
else:
    # Caso a requisição tenha falhado, exibe o código de erro e o texto da resposta
    print(f"Erro: {response.status_code}")
    print(response.text)

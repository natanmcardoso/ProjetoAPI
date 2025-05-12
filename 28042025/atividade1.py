#Criar um programa que:
#Peça um usuário para digitar a quantidade de cachorros que ele deseja buscar.
#Crie um limitador para controlar o input do usuário, não deixe que ele digite mais do que 5
#Faça um consulta de formato de lista na API da TheDogAPI, para buscar imagens aleatórias de cachorros.
#Mostre as informações de forma organizada para o usário

# Importa bibliotecas necessárias
import requests
import os
import webbrowser
from dotenv import load_dotenv
from datetime import datetime

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as chaves das APIs do ambiente
CAT_API_KEY = os.getenv('CAT_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# Verifica se as chaves foram carregadas corretamente
if not CAT_API_KEY:
    raise ValueError("A variável CAT_API_KEY não foi encontrada.")
if not NEWS_API_KEY:
    raise ValueError("A variável NEWS_API_KEY não foi encontrada.")
if not WEATHER_API_KEY:
    raise ValueError("A variável WEATHER_API_KEY não foi encontrada.")

# ===================== Função: Buscar Gatos =====================
def buscar_gatos():
    while True:
        try:
            quantidade = int(input("Quantos gatos você deseja ver? (máx. 5): "))
            if 1 <= quantidade <= 5:
                break
            else:
                print("Digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    url = f'https://api.thecatapi.com/v1/images/search?limit={quantidade}&has_breeds=1'
    headers = {'x-api-key': CAT_API_KEY}

    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"\n🐱 Exibindo {quantidade} imagem(ns) de gato(s):\n")

        for indice, item in enumerate(dados, start=1):
            url_imagem = item['url']
            print(f"{indice}. Imagem: {url_imagem}")
            webbrowser.open(url_imagem)

            if 'breeds' in item and item['breeds']:
                raca = item['breeds'][0]
                print(f"   📌 Raça: {raca.get('name', 'Desconhecida')}")
                print(f"   🧬 Temperamento: {raca.get('temperament', 'N/A')}")
                print(f"   🌍 Origem: {raca.get('origin', 'N/A')}")
                print(f"   🧪 Peso: {raca.get('weight', {}).get('metric', 'N/A')} kg")
                print(f"   ⏳ Expectativa de vida: {raca.get('life_span', 'N/A')} anos")
                print(f"   📖 Wikipedia: {raca.get('wikipedia_url', 'Não disponível')}\n")
            else:
                print("   ⚠️ Nenhuma informação de raça disponível.\n")
    else:
        print(f"Erro ao buscar gatos: {resposta.status_code}\n")

# ===================== Função: Buscar Notícias =====================
def buscar_noticias():
    termo = input("Digite um tema para buscar notícias (ex: Python, clima, esportes): ").strip()

    url = "https://newsapi.org/v2/everything"
    headers = {'x-api-key': NEWS_API_KEY}
    parametros = {
        'q': termo,
        'language': 'pt',
        'page': '1',
        'pageSize': 10
    }

    resposta = requests.get(url, headers=headers, params=parametros)

    if resposta.status_code == 200:
        resposta_json = resposta.json()
        artigos = resposta_json.get('articles', [])

        if not artigos:
            print("Nenhuma notícia encontrada para esse tema.")
            return

        print(f"\n📰 Exibindo notícias sobre: {termo}\n")
        for artigo in artigos[:10]:
            print(f"Título: {artigo['title']}")
            print(f"Descrição: {artigo['description']}")
            print(f"Link: {artigo['url']}")
            print("-" * 50)
    else:
        print(f"Erro ao buscar notícias: {resposta.status_code}")

# ===================== Função: Buscar Clima =====================
def obter_clima(cidade):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    parametros = {
        'q': cidade,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'pt_br'
    }

    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json()

        estado = dados['sys'].get('state', 'Desconhecido')
        pais = dados['sys']['country']

        if estado == 'Desconhecido' and ',' in cidade:
            estado = cidade.split(',')[1].strip().upper()

        nascer_sol = datetime.utcfromtimestamp(dados['sys']['sunrise']).strftime('%H:%M:%S')
        por_sol = datetime.utcfromtimestamp(dados['sys']['sunset']).strftime('%H:%M:%S')

        print(f"\n📍 Clima atual em {cidade}, {estado} ({pais}):")
        print(f"🌤️  Condição: {dados['weather'][0]['description']}")
        print(f"🌡️  Temperatura: {dados['main']['temp']}°C (Sensação térmica: {dados['main']['feels_like']}°C)")
        print(f"💧 Umidade: {dados['main']['humidity']}%")
        print(f"🍃 Vento: {dados['wind']['speed']} m/s")
        print(f"🌦️ Nuvens: {dados['clouds']['all']}%")
        print(f"📊 Pressão: {dados['main']['pressure']} hPa")
        print(f"🌅 Nascer do sol: {nascer_sol} UTC")
        print(f"🌇 Pôr do sol: {por_sol} UTC")
        print(f"👁️ Visibilidade: {dados['visibility'] / 1000} km\n")
    else:
        print(f"Erro ao consultar o clima para {cidade}. Código: {resposta.status_code}")

# ===================== Função: Buscar Clima de Múltiplas Cidades =====================
def buscar_clima():
    cidades = input("Digite as cidades (separadas por vírgula): ").split(",")
    for cidade in cidades:
        cidade = cidade.strip()
        obter_clima(cidade)

# ===================== Menu Principal =====================
while True:
    print("\n========= MENU =========")
    print("1. Ver imagens de gatos 🐱")
    print("2. Ver notícias 📰")
    print("3. Ver clima de cidades 🌦️")
    print("4. Sair ❌")
    print("========================")

    escolha = input("Escolha uma opção (1-4): ").strip()

    if escolha == '1':
        buscar_gatos()
    elif escolha == '2':
        buscar_noticias()
    elif escolha == '3':
        buscar_clima()
    elif escolha == '4':
        print("Você escolheu sair. Valeu, Falouuu! 👋")
        break
    else:
        print("Opção inválida. Tente novamente.")

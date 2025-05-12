import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Carregar variáveis de ambiente do .env
load_dotenv()

# Obter a API Key do ambiente
api_key = os.getenv('WEATHER_API_KEY')

# Função para buscar o clima de uma cidade
def obter_clima(cidade):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': cidade,          # Cidade e país
        'appid': api_key,     # Chave da API
        'units': 'metric',    # Unidades: metric (Celsius)
        'lang': 'pt_br'       # Idioma da resposta
    }

    # Fazer a requisição GET
    resposta = requests.get(url, params=params)

    # Verificar o status da requisição
    if resposta.status_code == 200:
        resposta_json = resposta.json()

        # Extrair as informações do estado e país
        estado = resposta_json['sys'].get('state', 'Desconhecido')  # Se não houver estado, 'Desconhecido'
        pais = resposta_json['sys']['country']

        # Se o estado estiver como 'Desconhecido' e a cidade estiver com a sigla do estado (exemplo: "olinda, pe"), vamos extrair a sigla
        if estado == 'Desconhecido' and ',' in cidade:
            estado = cidade.split(',')[1].strip().upper()

        # Converter timestamp de nascer e pôr do sol
        sunrise_time = datetime.utcfromtimestamp(resposta_json['sys']['sunrise']).strftime('%H:%M:%S')
        sunset_time = datetime.utcfromtimestamp(resposta_json['sys']['sunset']).strftime('%H:%M:%S')

        # Imprimir as informações
        print(f"\n📍 Clima atual em {cidade}, {estado} ({pais}):")
        print(f"🌤️  Condição: {resposta_json['weather'][0]['description']}")
        print(f"🌡️  Temperatura: {resposta_json['main']['temp']}°C (Sensação térmica: {resposta_json['main']['feels_like']}°C)")
        print(f"💧 Umidade: {resposta_json['main']['humidity']}%")
        print(f"🍃 Velocidade do vento: {resposta_json['wind']['speed']} m/s")
        print(f"🌦️ Nuvens: {resposta_json['clouds']['all']}%")
        print(f"📊 Pressão atmosférica: {resposta_json['main']['pressure']} hPa")
        print(f"🌅 Nascer do sol: {sunrise_time} UTC")
        print(f"🌇 Pôr do sol: {sunset_time} UTC")
        print(f"👁️ Visibilidade: {resposta_json['visibility'] / 1000} km\n")
    else:
        print(f"\nErro ao consultar o clima para a cidade {cidade}. Status Code: {resposta.status_code}")

# Função para solicitar a cidade do usuário
def buscar_clima():
    cidades = input("Digite as cidades que deseja consultar o clima (separadas por vírgula): ").split(",")
    
    for cidade in cidades:
        cidade = cidade.strip()  # Remove espaços em branco extras
        obter_clima(cidade)

# Chama a função de busca de clima
buscar_clima()

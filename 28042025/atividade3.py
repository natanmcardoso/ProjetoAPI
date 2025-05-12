#Crie um programa que:
#Para cada cidade, faça uma requisição à API da OpenWeather para verificar a temeperatura e o clima de cada cidade
#Apresente as informações de cada cidade de maneira formatada ao usuário
#Por fim, faça uma lógica que analisa e diga quais das cidades está mais quente
 
import requests
import os
from dotenv import load_dotenv
 
cidades = []    
temperaturas = {}
def consultar_clima():
    # Carregar variáveis de ambiente do .env
    load_dotenv()
 
    # Obter a API Key do ambiente
    api_key = os.getenv('WEATHER_API_KEY')
 
    if not api_key:
        raise ValueError('API Key não foi localizada nas variáveis de ambiente.')
 
    url = 'https://api.openweathermap.org/data/2.5/weather'
   
 
   
 
 
    for i in range(3):
        while True:
            cidade = input(f'Digite a cidade {i+1} para ver o clima: ')
            params = {
                'q': cidade,
                'appid': api_key,
                'units': 'metric',
                'lang': 'pt_br'
            }
           
   
            resposta = requests.get(url, params=params)
 
            if resposta.status_code == 200:
                dados = resposta.json()
                clima = dados['weather'][0]['description']
                temperatura = dados['main']['temp']
 
                print(f'\n Cidade válida!')
                print(f'O clima em {cidade} é: {clima}')
                print(f'A temperatura em {cidade} é: {temperatura}°C\n')
 
                cidades.append(cidade)
                temperaturas[cidade] = temperatura
                break
            else:
                print(f'Cidade "{cidade}" não encontrada. Tente novamente.')
                continue
           
 
    print(temperaturas)
 
def maior_temperatura():
    cidade_mais_quente = max(temperaturas, key=temperaturas.get)
    temp_max = temperaturas[cidade_mais_quente]
    print(f"\nA cidade mais quente é {cidade_mais_quente} com {temp_max:.2f}°C.")
 
 
 
 
consultar_clima()
maior_temperatura()
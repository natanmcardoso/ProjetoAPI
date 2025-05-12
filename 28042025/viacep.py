import time
import requests
 
cep = input('Digite seu CEP: ')
 
resultado = requests.get(f'https://viacep.com.br/ws/{cep}/json/')    
print(resultado.status_code)
 
resultado = resultado.json()
 
logradouro = resultado['logradouro']
complemento = resultado['complemento']
bairro = resultado['bairro']
 
print('Conectando com o banco de dados...')
time.sleep(2)
print('\n Informções salvas com sucesso!')
print('Logradouro: ', logradouro)
print('Complemento: ', complemento)
print('Bairro: ', bairro)
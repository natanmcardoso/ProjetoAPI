import requests  # Importa a biblioteca 'requests', usada para fazer requisições HTTP

# Faz uma requisição GET para obter um único post (com id = 1)
resposta_unique = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# Faz uma requisição GET para obter a lista completa de posts
resposta_lista = requests.get("https://jsonplaceholder.typicode.com/posts")

# Converte a resposta da lista de posts de JSON para um objeto Python (lista de dicionários)
posts = resposta_lista.json()
# Converte a resposta do post único de JSON para um objeto Python (um dicionário)
post_1 = resposta_unique.json()

# Mostra o tipo da variável 'posts' (esperado: list)
print("Tipo de lista (vários posts): ", type(posts))
# Mostra o tipo da variável 'post_1' (esperado: dict)
print("Tipo único (um só post): ", type(post_1))

# Percorre os 10 primeiros posts da lista
for post in posts[:10]:
    # Imprime o título do post
    print("Título:", post["title"])
    # Imprime o conteúdo (corpo) do post
    print("Conteúdo:", post["body"])

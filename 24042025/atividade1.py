def quantidade_posts(a):
    import requests
 
    resposta_lista = requests.get('https://jsonplaceholder.typicode.com/posts')
    resposta_unique = requests.get('https://jsonplaceholder.typicode.com/posts/1')
 
    posts = resposta_lista.json()
    post_1 = resposta_unique.json()
    print('Tipo de lista (vários posts): ', type(posts))
    print('Tipo único (um só post): ', type(post_1))
   
    for post in posts[:a]:
        print('Título: ', post['title'])
        print('Conteúdo: ', post['body'])
        print('-' * 50)
       
qntd = int(input('Digite a quantidade de posts que você quer ver: '))
 
quantidade_posts(qntd)
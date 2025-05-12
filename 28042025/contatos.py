# Agenda de contatos, agora com funções. Deverá conter as seguintes: 
# * Função menu para exibir as opções do sistema.
# * Função cadastrar contato.
# * Função editar contato. 
# * Função deletar contato.
# * Função mostrar contato.
# Deverá conter um laço principal para orquestrar o acesso as funções. 

contatos = []

def menu():
    """
    Exibe o menu principal com as opções disponíveis para o usuário.
    O menu permite o cadastro, edição, exclusão, exibição de contatos e a opção de sair.
    """
    print("-" * 35)
    print("MENU DO BENEFICIÁRIO INSS")
    print("-" * 35)
    print("1- Cadastro de um novo contato.")
    print("2- Editar um contato existente.")
    print("3- Deletar um contato existente.")
    print("4- Mostrar todos os contatos.")  
    print("5- Sair do sistema.")
    print("-" * 35)

def cadastrar_contato():
    """
    Solicita os dados (nome, e-mail, telefone) de um novo contato e o adiciona à lista de contatos.
    O código do novo contato é gerado automaticamente com base no tamanho da lista de contatos.
    """
    contato = {}
    contato["código"] = len(contatos)
    contato["nome"] = input('Digite o nome: ')
    contato["email"] = input('Digite o e-mail: ')
    contato["telefone"] = input('Digite o telefone: ')    
    contatos.append(contato)  
    print('Contato cadastrado com sucesso!!')

def editar_contato():
    """
    Permite ao usuário editar os dados (nome, e-mail, telefone) de um contato existente.
    O usuário deve fornecer o código do contato que deseja editar. Se o código for válido,
    ele pode alterar as informações do contato; caso contrário, é exibida uma mensagem de erro.
    """
    if not contatos:  # Verifica se a lista de contatos está vazia
        print("Não há contatos cadastrados para editar.")
        return  # Retorna da função, sem fazer nada
    
    print("\nLista de contatos disponíveis para edição:")
    mostrar_contatos()  # Exibe todos os contatos para o usuário escolher

    codigo = int(input("\nDigite o código do contato que deseja editar:"))
    
    if codigo >= 0 and codigo < len(contatos):
        print("Contato atual", contatos[codigo])
        nome = input("Digite o novo nome (ou deixe em branco para manter o mesmo):")
        email = input("Digite o novo email (ou deixe em branco para manter o mesmo):")
        telefone = input("Digite o novo telefone (ou deixe em branco para manter o mesmo):")
        
        if nome: 
            contatos[codigo]["nome"] = nome
        if email: 
            contatos[codigo]["email"] = email
        if telefone: 
            contatos[codigo]["telefone"] = telefone
        
        print("Contato atualizado com sucesso!")
    else:
        print("Código inválido!")


def deletar_contato():
    """
    Permite ao usuário deletar um contato existente com base no código fornecido.
    O contato será removido da lista, e os códigos dos contatos subsequentes serão atualizados.
    Se o código fornecido for inválido, é exibida uma mensagem de erro.
    """
    mostrar_contatos()  # Exibe todos os contatos para o usuário escolher
    
    if not contatos:  # Verifica se a lista de contatos está vazia
        print("Não há contatos cadastrados para editar.")
        return  # Retorna da função, sem fazer nada
      
    codigo = int(input("Digite o código do contato que deseja deletar:"))
      
    if codigo >= 0 and codigo < len(contatos):
        contatos.pop(codigo)
        
        # Atualiza os códigos dos contatos após a remoção
        for i in range(len(contatos)):
            contatos[i]["código"] = i
        
        print("Contato deletado com sucesso!")
    else:
        print("Código inválido!")

def mostrar_contatos():
    """
    Exibe todos os contatos cadastrados na lista. 
    Caso não haja contatos cadastrados, exibe uma mensagem informando que não há nenhum contato.
    """
    if contatos:
        print("\nLista de contatos:")
        for contato in contatos:
            print(contato)
    else:
        print("Nenhum contato cadastrado.")

while True:
    menu()
    opcao = input('Escolha uma das opções acima (ou 5 para sair do sistema): ').title()
    
    if opcao == "5":
        print("Saindo do sistema do INSS...")
        break
    
    if opcao == "1":
        cadastrar_contato()
    elif opcao == "2":
        editar_contato()
    elif opcao == "3":
        deletar_contato()
    elif opcao == "4":
        mostrar_contatos()
    else:
        print("Opção inválida, tente novamente.")
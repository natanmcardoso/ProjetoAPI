import requests

contatos = []

def menu():
    """
    Exibe o menu principal com emojis para tornar mais visual.
    """
    print("\n📒 MENU DO BENEFICIÁRIO INSS")
    print("-" * 40)
    print("1️⃣  Cadastrar novo contato")
    print("2️⃣  ✏️ Editar contato existente")
    print("3️⃣  🗑️ Deletar contato")
    print("4️⃣  📋 Mostrar todos os contatos")
    print("5️⃣  🚪 Sair do sistema")
    print("-" * 40)

def obter_endereco_pelo_cep(cep):
    """
    Consulta a API do ViaCEP para obter o endereço baseado no CEP.
    Retorna o endereço formatado ou None se o CEP for inválido.
    """
    try:
        resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                endereco = f"{dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}"
                return endereco
    except Exception:
        pass
    return None

def cadastrar_contato():
    """
    Cadastra um novo contato com nome, email, telefone e endereço via CEP.
    """
    print("\n📝 CADASTRO DE NOVO CONTATO")
    nome = input('👤 Nome: ')
    email = input('📧 E-mail: ')
    telefone = input('📱 Telefone: ')
    
    while True:
        cep = input('🏠 CEP (somente números): ')
        if cep.isdigit() and len(cep) == 8:
            endereco = obter_endereco_pelo_cep(cep)
            if endereco:
                break
            else:
                print("❌ CEP inválido ou não encontrado. Tente novamente.")
        else:
            print("⚠️ CEP inválido. Digite apenas 8 números.")
    
    contato = {
        "código": len(contatos),
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "endereço": endereco
    }
    contatos.append(contato)
    print("✅ Contato cadastrado com sucesso!")

def editar_contato():
    """
    Permite editar os dados de um contato existente.
    """
    if not contatos:
        print("⚠️ Não há contatos cadastrados.")
        return

    mostrar_contatos()
    try:
        codigo = int(input("\n🔎 Código do contato a editar: "))
        if 0 <= codigo < len(contatos):
            contato = contatos[codigo]
            print(f"\n✏️ Editando contato: {contato['nome']}")
            
            novo_nome = input("👤 Novo nome (enter para manter): ")
            novo_email = input("📧 Novo email (enter para manter): ")
            novo_telefone = input("📱 Novo telefone (enter para manter): ")
            
            if novo_nome:
                contato["nome"] = novo_nome
            if novo_email:
                contato["email"] = novo_email
            if novo_telefone:
                contato["telefone"] = novo_telefone

            alterar_endereco = input("Deseja alterar o endereço? (s/n): ").lower()
            if alterar_endereco == 's':
                while True:
                    novo_cep = input('🏠 Novo CEP (somente números): ')
                    if novo_cep.isdigit() and len(novo_cep) == 8:
                        novo_endereco = obter_endereco_pelo_cep(novo_cep)
                        if novo_endereco:
                            contato["endereço"] = novo_endereco
                            break
                        else:
                            print("❌ CEP inválido ou não encontrado.")
                    else:
                        print("⚠️ CEP inválido.")
            
            print("✅ Contato atualizado com sucesso!")
        else:
            print("❌ Código inválido.")
    except ValueError:
        print("❗ Entrada inválida. Digite apenas números.")

def deletar_contato():
    """
    Remove um contato da lista pelo código.
    """
    if not contatos:
        print("⚠️ Não há contatos cadastrados.")
        return

    mostrar_contatos()
    try:
        codigo = int(input("\n🗑️ Código do contato a deletar: "))
        if 0 <= codigo < len(contatos):
            contatos.pop(codigo)
            for i in range(len(contatos)):
                contatos[i]["código"] = i
            print("✅ Contato deletado com sucesso.")
        else:
            print("❌ Código inválido.")
    except ValueError:
        print("❗ Entrada inválida. Digite apenas números.")

def mostrar_contatos():
    """
    Exibe todos os contatos com formatação legível e emojis.
    """
    if not contatos:
        print("\n📭 Nenhum contato cadastrado.")
        return

    print("\n📋 LISTA DE CONTATOS")
    print("-" * 40)
    for contato in contatos:
        print(f"🔢 Código  : {contato['código']}")
        print(f"👤 Nome    : {contato['nome']}")
        print(f"📧 E-mail  : {contato['email']}")
        print(f"📱 Telefone: {contato['telefone']}")
        print(f"🏠 Endereço: {contato['endereço']}")
        print("-" * 40)

# Laço principal
while True:
    menu()
    opcao = input("📌 Escolha uma opção (1 a 5): ")

    if opcao == "1":
        cadastrar_contato()
    elif opcao == "2":
        editar_contato()
    elif opcao == "3":
        deletar_contato()
    elif opcao == "4":
        mostrar_contatos()
    elif opcao == "5":
        print("👋 Saindo do sistema... Até logo!")
        break
    else:
        print("❗ Opção inválida. Tente novamente.")

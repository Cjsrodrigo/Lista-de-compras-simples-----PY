import .uuid

def exibir_cabecalho():
    print()
    print("Lista de Compras Simples")
    print("Bem-vindo ao aplicativo de lista de compras!\n")

def menu():
    print()
    print("Menu:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Pesquisar produtos")
    print("4. Sair")



def listar_produtos(produtos):
    if produtos:
        print()
        print("Lista de Produtos:")
        for produto_id, produto in produtos.items():
            print(f"ID: {produto_id} | Nome: {produto['nome']} | Unidade: {produto['unidade']} | Quantidade: {produto['quantidade']} | Descrição: {produto['descricao']}")
    else:
        print("A lista está vazia.")

def adicionar_produto(produtos):
    nome = input("Digite o nome do produto: ")
    unidade = input("Digite a unidade de medida (Quilograma, Grama, Litro, Mililitro, Unidade, Metro, Centímetro): ")

    unidades_validas = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]
    while unidade not in unidades_validas:
        print("Unidade inválida. Por favor, escolha uma das unidades listadas.")
        unidade = input("Digite a unidade de medida (Quilograma, Grama, Litro, Mililitro, Unidade, Metro, Centímetro): ")

    try:
        quantidade = float(input("Digite a quantidade do produto: "))
    except ValueError:
        print("Quantidade inválida. Digite um número válido.")
        return

    descricao = input("Digite uma descrição para o produto: ")



    produto_id = str(uuid.uuid4())
    produtos[produto_id] = {
        'nome': nome,
        'unidade': unidade,
        'quantidade': quantidade,
        'descricao': descricao
    }

    print(f"Produto '{nome}' adicionado com sucesso!")



def remover_produto(produtos):

        produto_id = input("Digite o ID do produto que deseja remover: ")
        if produto_id in produtos:
            del produtos[produto_id]
            print(f"Produto com ID '{produto_id}' removido com sucesso!")
        else:
            print("ID do produto não encontrado.")

def pesquisar_produtos(produtos):
    termo = input("Digite o nome ou parte do nome do produto para pesquisa: ").lower()
    resultados = [produto for produto in produtos.values() if termo in produto['nome'].lower()]

    if resultados:
        print()
        print(f"Foram encontrados {len(resultados)} produto(s):")
        for produto in resultados:
            print(f"Nome: {produto['nome']} | Unidade: {produto['unidade']} | Quantidade: {produto['quantidade']} | Descrição: {produto['descricao']}")
    else:
        print("Nenhum produto encontrado com esse nome.")


def funcionalidade():
    produtos = {}

    while True:
        exibir_cabecalho()
        listar_produtos(produtos)
        menu()

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            adicionar_produto(produtos)
        elif opcao == '2':
            remover_produto(produtos)
        elif opcao == '3':
            pesquisar_produtos(produtos)
        elif opcao == '4':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

funcionalidade()

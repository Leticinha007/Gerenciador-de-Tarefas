# Gerenciador de Tarefas em Python 3
# Desenvolvido por: Douglas Dos Santos Ferraz e Leticia Rebeka Ferreira Felix

# Lista para armazenar as tarefas, inicialmente vazia
tarefas = []

def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis para o usuário.
    """
    print("\nGerenciador de Tarefas")
    print("1. Cadastrar nova tarefa")
    print("2. Listar tarefas pendentes")
    print("3. Listar tarefas concluídas")
    print("4. Editar tarefa")
    print("5. Marcar tarefa como concluída")
    print("6. Excluir tarefa")
    print("7. Sair")

def cadastrar_tarefa():
    """
    Solicita ao usuário a descrição de uma nova tarefa e adiciona à lista de tarefas 
    com o status inicial 'pendente'.
    """
    descricao = input("Digite a descrição da tarefa: ")
    # Cada tarefa é um dicionário contendo a descrição e o status
    tarefa = {'descricao': descricao, 'status': 'pendente'}
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")

def listar_tarefas(status):
    """
    Lista as tarefas com base no status fornecido (pendente ou concluída).
    
    Args:
        status (str): O status das tarefas que serão listadas ('pendente' ou 'concluída').
    """
    print(f"\nTarefas {status}s:")
    encontrou = False  # Variável para verificar se existem tarefas a listar
    for idx, tarefa in enumerate(tarefas):
        if tarefa['status'] == status:
            print(f"{idx + 1}. {tarefa['descricao']}")
            encontrou = True
    if not encontrou:
        print(f"Nenhuma tarefa {status} encontrada.")

def editar_tarefa():
    """
    Permite que o usuário edite a descrição de uma tarefa pendente.
    Exibe a lista de tarefas pendentes para escolha.
    """
    listar_tarefas('pendente')
    indice = int(input("Digite o número da tarefa que deseja editar: ")) - 1
    if 0 <= indice < len(tarefas) and tarefas[indice]['status'] == 'pendente':
        nova_descricao = input("Digite a nova descrição: ")
        tarefas[indice]['descricao'] = nova_descricao
        print("Tarefa editada com sucesso!")
    else:
        print("Tarefa inválida ou já concluída.")

def marcar_como_concluida():
    """
    Marca uma tarefa pendente como concluída.
    O usuário escolhe a tarefa da lista de pendentes para atualizar o status.
    """
    listar_tarefas('pendente')
    indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
    if 0 <= indice < len(tarefas) and tarefas[indice]['status'] == 'pendente':
        tarefas[indice]['status'] = 'concluída'
        print("Tarefa marcada como concluída!")
    else:
        print("Tarefa inválida ou já concluída.")

def excluir_tarefa():
    """
    Exclui uma tarefa pendente escolhida pelo usuário.
    Exibe a lista de tarefas pendentes para escolha.
    """
    listar_tarefas('pendente')
    indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
    if 0 <= indice < len(tarefas) and tarefas[indice]['status'] == 'pendente':
        tarefas.pop(indice)
        print("Tarefa excluída com sucesso!")
    else:
        print("Tarefa inválida ou já concluída.")

def main():
    """
    Função principal que controla o fluxo do programa. Exibe o menu e chama as funções 
    de acordo com a escolha do usuário.
    """
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_tarefa()
        elif opcao == '2':
            listar_tarefas('pendente')
        elif opcao == '3':
            listar_tarefas('concluída')
        elif opcao == '4':
            editar_tarefa()
        elif opcao == '5':
            marcar_como_concluida()
        elif opcao == '6':
            excluir_tarefa()
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Verifica se o script está sendo executado diretamente e inicia o programa
if __name__ == "__main__":
    main()

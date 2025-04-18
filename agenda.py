# Agenda de Tarefas Simples

tarefas = []

# Função para mostrar as tarefas
def mostrar_tarefas():
    print("\nSuas tarefas:")
    for idx, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{idx + 1}. {tarefa['descricao']} - {status}")

# Menu de opções
while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Concluir tarefa")
    print("3 - Mostrar tarefas")
    print("4 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        descricao = input("Digite a descrição da tarefa: ")
        tarefas.append({"descricao": descricao, "concluida": False})
    elif escolha == '2':
        mostrar_tarefas()
        num = int(input("Digite o número da tarefa a concluir: "))
        if 0 < num <= len(tarefas):
            tarefas[num - 1]['concluida'] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido!")
    elif escolha == '3':
        mostrar_tarefas()
    elif escolha == '4':
        print("Saindo da Agenda. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")

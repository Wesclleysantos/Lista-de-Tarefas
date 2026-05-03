def menu():
    print("\nMenu:")
    print("1- Adicionar tarefa")
    print("2- Listar tarefa")
    print("3- remover tarefa")
    print("0- Sair do programa")

def adicionar(lista):
    tarefa = input("Digite a tarefa: ")
    lista.append(tarefa)
    salvar(lista)
    print("Tarefa adicionada com sucesso!")

def listar(lista):
    if not lista:
        print("Nenhuma tarefa na lista.")
        return
    for i, item in enumerate(lista, start=1):
        print(f"{i} - {item}")

def remover(lista):
    if not lista:
        print("Lista vazia!")
        return
    
    try:
        r = int(input("Digite o número da tarefa: "))
        removida = lista.pop(r - 1)
        salvar(lista)
        print(f"Tarefa '{removida}' removida com sucesso!")
    except (ValueError, IndexError):
        print("Erro: Índice inválido!")

def salvar(lista):
    with open("tarefa.txt", "w", encoding="utf-8") as arquivo:
        for tarefa in lista:
            arquivo.write(tarefa + "\n")

def carregar():
    try:
        with open("tarefa.txt", "r", encoding="utf-8") as arquivo:
            return [linha.strip() for linha in arquivo]
    except FileNotFoundError:
        return []
    
import tarefa as t
lista = []
while True:
    t.menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        t.adicionar(lista)
    
    elif escolha == "2":
        t.listar(lista)

    elif escolha == "3":
        t.remover(lista)
    
    elif escolha == "0":
        print("Saindo do programa. . .")
        break
    else: print("Opção inválida!")
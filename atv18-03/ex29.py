def exibir_menu():
    print("Bem vindo ao menu dos cachorros quadrados doidos")
    print("1 - Novo cadastro de um cachorro quadrado doido")
    print("2 - Ver perfil cachorro quadrado doido")
    print("3 - Sair")
    print("---------------------")

def cadastrar_cachorro (cadastros):
    nome = input("Nome:")
    idade = input("Idade:")
    doidera = input("Doidera:")
    Demencia = input("Demencia:") 
    cadastros.append({"Nome":nome, "idade":idade, "Doidera":doidera, "demencia":Demencia})
    print("Cadastro realizado com sucesso")
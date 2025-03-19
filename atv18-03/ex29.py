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
    cadastros.append({"Nome":nome, "Idade":idade, "Doidera":doidera, "demencia":Demencia})
    print("Cadastro realizado com sucesso")

def ver_cadastros (cadastros):
    if not cadastros:
        print("Nenhum cachorro doido no sistema.")
    else:
        print("\n ------- LISTA DE CADASTROS DE DOGS DOIDOS-------")

        for i, pessoa in enumerate (cadastros,1):

            print(f'{i} . nome: {pessoa['nome']}, idade:{pessoa ['idade']}, doidera: {pessoa['doidera']}, demencia: {pessoa['demencia']}')
                  
def main():
    cadastros = []
    while True:
        exibir_menu()
        opção = input("escolha uma opção:")
            
        if opção == "1":
               cadastrar_cachorro(cadastros)

        elif opção == "2":
               ver_cadastros (cadastros)

        elif opção == "3":
             print("Obrigado por utilizar o sistema cadastrerdogcrazy")
             break
        else:
             print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
       main()             

               

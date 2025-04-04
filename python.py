import json 

arquivo_cadastros = "cadastros.json"    

def exibir_menu():
    print("\n ---- MENU CADASTRO")  
    print("1 - cadastrar pessoa")
    print("2 - ver cadatro")
    print("3 - sair")
    print("----------------")

def salvar_cadastros (cadastros):
    with open (arquivo_cadastro, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)
        
def carregar_cadastros():
     try:
        with open (arquivo_cadastros, "r", encoding="utf-8") as arquivo:
           return json.load(arquivo)
      except (FileNotFoundError, json.JSONDecodeError):
        return []

def cadastrar_cachorro (cadastros):
    nome = input("Nome:")
    idade = input("Idade:")
    doidera = input("Doidera:")
    Demencia = input("Demencia:")

    cadastros.append({"Nome":nome, "Idade":idade, "Doidera":doidera, "demencia":Demencia})
    salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso!")

    #paramos no dia 04/04/2025
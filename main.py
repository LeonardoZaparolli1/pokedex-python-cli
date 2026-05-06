import datetime
import json



def carregar_pokemons():
    try:
        with open("pokemons.json", "r") as dados_pokemon:
            return json.load(dados_pokemon)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("O arquivo esta corrompido ou vazio, criando um novo arquivo")
        return []
    
pokemons = carregar_pokemons()

def salvar_pokemons(lista_pokemons):
    with open("pokemons.json", "w") as dados_pokemon:
        json.dump(lista_pokemons, dados_pokemon, indent=4)
    

def exibir_about():
    print("Bem vindo ao software de gestão de pokedex do treinador pokemon Leonardo Zaparolli")


def encontrar_pokemon(lista_pokemons, nome):
    for elemento in lista_pokemons:
        if elemento["nome"].lower() == nome.lower():
            return elemento
    return None


def adicionar_pokemons(lista_pokemons):
    while True:
        try:
            num_pokemons = int(input("Quantos pokemons deseja adicionar a pokedex? "))

            if num_pokemons <= 0:
                print("ERRO, numero de pokemons não pode ser negativo, nem zero, tente novamente")
            else:
                for i in range(num_pokemons):
                    nome_pokemon = str(input(f"Digite o nome do pokemon: "))
                    tipo_pokemon = str(input(f"Digite o tipo do pokemon: "))

                    while True:
                        shiny_pokemon = (input(f"o pokemon é shiny? Digite sim ou não: ")).upper()
                        if shiny_pokemon == "SIM":
                            shiny_pokemon = True
                            break
                        elif shiny_pokemon == "NÃO" or shiny_pokemon == "NAO":
                            shiny_pokemon = False
                            break
                        else:
                            print("ERRO, valor digitado para shiny é inválido, tente novamente")

                    print(f"Pokemon adicionado a pokedex: Nome: {nome_pokemon}, Tipo: {tipo_pokemon}, shiny: {shiny_pokemon}")
                    cadastro_pokemon = {
                        "nome": nome_pokemon,
                        "tipo": tipo_pokemon,
                        "shiny": shiny_pokemon,
                        "historico": []
                    }
                    lista_pokemons.append(cadastro_pokemon)
                break

        except ValueError:
            print("ERRO, valor digitado não é um número inteiro, tente novamente")


def listar_pokemons(lista_pokemons):
    if lista_pokemons == []:
        print("Você não tem nenhum pokemon registrado, use o comando add para registrar seus Pokemons")
    else:
        print("Lista de pokemons registrados: ")
        for p in lista_pokemons:
            for chave, valor in p.items():
                print(f"{chave}: {valor}")
            print(" ")


def atualizar_pokemon(lista_pokemons):
    if lista_pokemons == []:
        print("Você não tem nenhum pokemon registrado, use o comando add para registrar seus Pokemons")
        return
    try:
        modificar_pokemon = input(str("Qual pokemon deseja atualizar? "))
    except ValueError:
        print("ERRO, valor digitado é inválido, tente novamente")
        return
    
    elemento = encontrar_pokemon(lista_pokemons, modificar_pokemon)

    if elemento is None:
        print("Pokemon não encontrado, tente novamente")
        return

    nome_antigo = elemento["nome"]
    tipo_antigo = elemento["tipo"]
    shiny_antigo = elemento["shiny"]

    data_atualizacao = datetime.datetime.now()
    try:
        elemento["nome"] = input(str("Digite o novo nome do pokemon: "))
        elemento["tipo"] = input(str("Digite o novo tipo do pokemon: "))
    except ValueError:
        print("ERRO, valor digitado é inválido, tente novamente")
        return

    while True:
        try:
            shiny_novo = (input("O pokemon é shiny? Digite sim ou não: ")).upper()
        except ValueError:
            print("ERRO, valor digitado é inválido, tente novamente")
            return
        
        if shiny_novo == "SIM":
            elemento["shiny"] = True
            break
        elif shiny_novo == "NÃO" or shiny_novo == "NAO":
            elemento["shiny"] = False
            break
        else:
            print("ERRO, valor digitado para shiny é inválido, tente novamente")

    print(f"Pokemon atualizado com sucesso, novo nome: {elemento['nome']}, novo tipo: {elemento['tipo']}, shiny: {elemento['shiny']}, data da atualização: {data_atualizacao}")
    registro_historico = (str(data_atualizacao), nome_antigo, elemento["nome"], tipo_antigo, elemento["tipo"], shiny_antigo, elemento["shiny"])
    elemento["historico"].append(registro_historico)


def deletar_pokemon(lista_pokemons):
    if lista_pokemons == []:
        print("Você não tem nenhum pokemon registrado, use o comando add para registrar seus Pokemons")
        return

    try:
        deletar = input(str("Qual pokemon deseja deletar? "))
    except ValueError:
        print("ERRO, valor digitado é inválido, tente novamente")
        return
    elemento = encontrar_pokemon(lista_pokemons, deletar)

    if elemento is None:
        print("Pokemon não encontrado, tente novamente")
        return

    lista_pokemons.remove(elemento)
    print(f"Pokemon {deletar} deletado com sucesso")

while True:
    try:
        print("Digite um dos comandos para acessar informações do software: \n - About  \n - Add \n - List \n - Update \n - Delete \n - Quit")
        
        comando = input("Digite o comando: ").upper()

        if comando == "ABOUT":
            exibir_about()
        
        elif comando == "ADD":
            adicionar_pokemons(pokemons)

        elif comando == "LIST":
            listar_pokemons(pokemons)

        elif comando == "UPDATE":
            atualizar_pokemon(pokemons)

        elif comando == "DELETE":
            deletar_pokemon(pokemons)

        elif comando == "QUIT":
            salvar_pokemons(pokemons)
            print("Saindo do gestor de pokedex")
            print("Até a proxima, treinador (\\__/)")
            break

        else:
            print("ERRO, comando não reconhecido, tente novamente")
    except ValueError:
        print("ERRO, valor digitado é inválido, tente novamente")
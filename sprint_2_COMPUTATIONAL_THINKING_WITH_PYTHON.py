# ============================================================
#  StudyLens - Sistema de Gerenciamento de Estudos
#  Projeto: Jovi x Faculdade - Engenharia de Software
#  Integrantes :
#    - Anna Carolina Fortes de Paula \ Rm:570544
#    - Arthur Machado Romão \ Rm:568878
#    - Henrique Cortez Ludovino \ Rm:571366
#    - Henrique Ferreira de Amorim \ Rm:570740
#    - Vinícius Ribeiro Silva Romão \ Rm:564379
# ============================================================

# Lista principal que armazena as matérias cadastradas
# Cada matéria é um dicionário com nome e lista de registros
materias = []


# ------------------------------------------------------------
# FUNÇÕES AUXILIARES
# ------------------------------------------------------------

def linha():
    """Imprime uma linha separadora para organizar o menu."""
    print("-" * 45)


def pausar():
    """Pausa a execução até o usuário pressionar Enter."""
    input("\nPressione Enter para voltar ao menu...")


def buscar_materia(nome_busca):
    """
    Busca uma matéria na lista pelo nome.
    Retorna o índice se encontrar, ou -1 se não encontrar.
    """
    for i in range(len(materias)):
        if materias[i]["nome"].lower() == nome_busca.lower():
            return i
    return -1


# ------------------------------------------------------------
# FUNCIONALIDADE 1 - Cadastrar Matéria
# ------------------------------------------------------------

def cadastrar_materia():
    """Permite ao usuário cadastrar uma nova matéria no sistema."""
    linha()
    print("  CADASTRAR MATÉRIA")
    linha()

    # Validação: nome não pode ser vazio
    while True:
        nome = input("Nome da matéria: ").strip()
        if nome == "":
            print("Erro: o nome não pode ser vazio. Tente novamente.")
        else:
            break

    # Verifica se a matéria já existe
    if buscar_materia(nome) != -1:
        print(f"\nAtenção: a matéria '{nome}' já está cadastrada!")
        pausar()
        return

    # Cadastra a nova matéria com lista de registros vazia
    nova_materia = {
        "nome": nome,
        "registros": []
    }
    materias.append(nova_materia)

    print(f"\nMatéria '{nome}' cadastrada com sucesso!")
    pausar()


# ------------------------------------------------------------
# FUNCIONALIDADE 2 - Registrar Foto/Anotação
# ------------------------------------------------------------

def registrar_foto():
    """Registra uma anotação de aula em uma matéria existente."""
    linha()
    print("  REGISTRAR ANOTAÇÃO DE AULA")
    linha()

    # Verifica se há matérias cadastradas
    if len(materias) == 0:
        print("Nenhuma matéria cadastrada ainda.")
        print("Vá ao menu e escolha a opção 1 primeiro.")
        pausar()
        return

    # Lista as matérias disponíveis
    print("Matérias disponíveis:")
    for i in range(len(materias)):
        print(f"  {i + 1}. {materias[i]['nome']}")

    linha()

    # Validação: o usuário deve digitar o nome correto
    nome_materia = input("Digite o nome da matéria: ").strip()
    indice = buscar_materia(nome_materia)

    if indice == -1:
        print(f"\nMatéria '{nome_materia}' não encontrada!")
        pausar()
        return

    # Coleta os dados da anotação
    print(f"\nRegistrando anotação para: {materias[indice]['nome']}")
    linha()

    # Validação: data no formato DD/MM/AAAA
    while True:
        data = input("Data da aula (DD/MM/AAAA): ").strip()
        if len(data) == 10 and data[2] == "/" and data[5] == "/":
            break
        else:
            print("Formato inválido! Use DD/MM/AAAA. Tente novamente.")

    # Validação: conteúdo não pode ser vazio
    while True:
        conteudo = input("Conteúdo visto na aula: ").strip()
        if conteudo == "":
            print("Erro: o conteúdo não pode ser vazio. Tente novamente.")
        else:
            break

    # Pergunta se a foto foi tirada (sim/não)
    while True:
        foto = input("Foto da lousa tirada? (S/N): ").strip().upper()
        if foto == "S" or foto == "N":
            break
        else:
            print("Digite apenas S ou N.")

    # Monta o registro e adiciona na lista da matéria
    registro = {
        "data": data,
        "conteudo": conteudo,
        "foto": foto
    }
    materias[indice]["registros"].append(registro)

    # Exibe confirmação com f-string
    status_foto = "Sim" if foto == "S" else "Não"
    print(f"\nAnotação registrada com sucesso!")
    print(f"  Matéria : {materias[indice]['nome']}")
    print(f"  Data    : {data}")
    print(f"  Conteúdo: {conteudo}")
    print(f"  Foto    : {status_foto}")

    pausar()


# ------------------------------------------------------------
# FUNCIONALIDADE 3 - Visualizar Resumo das Matérias
# ------------------------------------------------------------

def visualizar_resumo():
    """Exibe o resumo completo de todas as matérias e seus registros."""
    linha()
    print("  RESUMO DAS MATÉRIAS")
    linha()

    # Verifica se há matérias cadastradas
    if len(materias) == 0:
        print("Nenhuma matéria cadastrada ainda.")
        pausar()
        return

    # Percorre todas as matérias com for
    for materia in materias:
        total_registros = len(materia["registros"])
        print(f"\nMatéria: {materia['nome']}")
        print(f"Total de aulas registradas: {total_registros}")

        if total_registros == 0:
            print("  Nenhuma anotação registrada ainda.")
        else:
            # Conta quantas aulas tiveram foto
            fotos_tiradas = 0
            for reg in materia["registros"]:
                if reg["foto"] == "S":
                    fotos_tiradas += 1

            print(f"Aulas com foto da lousa: {fotos_tiradas} de {total_registros}")
            linha()

            # Lista cada registro da matéria
            for i in range(len(materia["registros"])):
                reg = materia["registros"][i]
                status_foto = "Com foto" if reg["foto"] == "S" else "Sem foto"
                print(f"  Aula {i + 1} | {reg['data']} | {status_foto}")
                print(f"  Conteudo: {reg['conteudo']}")
                print()

        linha()

    pausar()


# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------

def menu_principal():
    """Exibe o menu principal e controla a navegação do sistema."""
    while True:
        print("\n")
        linha()
        print("       STUDYLENS - SISTEMA DE ESTUDOS")
        linha()
        print("  1. Cadastrar matéria")
        print("  2. Registrar anotação de aula")
        print("  3. Visualizar resumo das matérias")
        print("  4. Sair")
        linha()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_materia()
        elif opcao == "2":
            registrar_foto()
        elif opcao == "3":
            visualizar_resumo()
        elif opcao == "4":
            print("\nSaindo do StudyLens. Até mais!")
            break
        else:
            print("Opção inválida! Digite 1, 2, 3 ou 4.")


# ------------------------------------------------------------
# INÍCIO DO PROGRAMA
# ------------------------------------------------------------

menu_principal()

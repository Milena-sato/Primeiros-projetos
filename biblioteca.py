import json
import os

# Define o caminho do arquivo no diretório de trabalho atual
DIRETORIO_SCRIPT = os.getcwd()
ARQUIVO_DADOS = os.path.join(DIRETORIO_SCRIPT, "biblioteca.json")

# Lista global para armazenar os livros em memória
acervo = []


def carregar_dados():
    """Carrega os livros armazenados no arquivo JSON ao iniciar o programa."""
    global acervo
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                acervo = json.load(arquivo)
        except Exception as e:
            print(f"Erro ao carregar os dados: {e}")
            acervo = []
    else:
        # Se o arquivo não existir, inicia acervo com 5 livros pré-cadastrados
        acervo = [
            {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "disponivel": "Sim"},
            {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890, "disponivel": "Sim"},
            {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": "Sim"},
            {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954, "disponivel": "Sim"},
            {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943, "disponivel": "Sim"}
        ]
        salvar_dados()


def salvar_dados():
    """Salva a lista de livros no arquivo JSON."""
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(acervo, arquivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")


def cadastrar_livro():
    """Cadastra um novo livro no acervo."""
    print("\n--- CADASTRO DE LIVRO ---")
    titulo = input("Título do livro: ").strip()
    autor = input("Autor: ").strip()
    
    while True:
        try:
            ano = int(input("Ano de publicação: "))
            break
        except ValueError:
            print("Por favor, digite um ano válido (número inteiro).")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": "Sim"
    }

    acervo.append(livro)
    salvar_dados()
    print(f"Livro '{titulo}' cadastrado com sucesso!")


def listar_livros():
    """Exibe todos os livros do acervo."""
    print("\n--- ACERVO DA BIBLIOTECA ---")
    if not acervo:
        print("Nenhum livro cadastrado no sistema.")
        return

    for idx, livro in enumerate(acervo, start=1):
        print(f"{idx}. Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Disponível: {livro['disponivel']}")


def buscar_livro():
    """Busca livros por título ou autor."""
    print("\n--- BUSCA DE LIVROS ---")
    termo = input("Digite o título ou autor para busca: ").strip().lower()
    resultados = [l for l in acervo if termo in l["titulo"].lower() or termo in l["autor"].lower()]

    if resultados:
        print(f"\n{len(resultados)} resultado(s) encontrado(s):")
        for livro in resultados:
            print(f"- Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Disponível: {livro['disponivel']}")
    else:
        print("Nenhum livro encontrado com o termo informado.")


def emprestar_livro():
    """Altera o status do livro para 'Não'."""
    print("\n--- EMPRÉSTIMO DE LIVRO ---")
    titulo = input("Digite o título do livro que deseja pegar emprestado: ").strip().lower()
    
    for livro in acervo:
        if livro["titulo"].lower() == titulo:
            if livro["disponivel"] == "Sim":
                livro["disponivel"] = "Não"
                salvar_dados()
                print(f"Empréstimo realizado com sucesso! O livro '{livro['titulo']}' foi reservado.")
            else:
                print(f"O livro '{livro['titulo']}' já está emprestado no momento.")
            return

    print("Livro não encontrado no acervo.")


def devolver_livro():
    """Reverte o status do livro para 'Sim'."""
    print("\n--- DEVOLUÇÃO DE LIVRO ---")
    titulo = input("Digite o título do livro que deseja devolver: ").strip().lower()

    for livro in acervo:
        if livro["titulo"].lower() == titulo:
            if livro["disponivel"] == "Não":
                livro["disponivel"] = "Sim"
                salvar_dados()
                print(f"Devolução realizada com sucesso! O livro '{livro['titulo']}' está disponível novamente.")
            else:
                print(f"O livro '{livro['titulo']}' já se encontra na biblioteca.")
            return

    print("Livro não encontrado no acervo.")


def exibir_estatisticas():
    """Exibe estatísticas sobre o acervo."""
    total = len(acervo)
    disponiveis = sum(1 for l in acervo if l["disponivel"] == "Sim")
    emprestados = total - disponiveis

    print("\n--- ESTATÍSTICAS DO ACERVO ---")
    print(f"Total de livros cadastrados: {total}")
    print(f"Livros disponíveis: {disponiveis}")
    print(f"Livros emprestados: {emprestados}")


def remover_livro():
    """Remove um livro do sistema."""
    print("\n--- REMOÇÃO DE LIVRO ---")
    titulo = input("Digite o título do livro que deseja remover: ").strip().lower()

    for livro in acervo:
        if livro["titulo"].lower() == titulo:
            acervo.remove(livro)
            salvar_dados()
            print(f"O livro '{livro['titulo']}' foi removido com sucesso!")
            return

    print("Livro não encontrado no acervo.")


def menu_principal():
    """Exibe o menu principal e faz a gestão do fluxo."""
    carregar_dados()

    while True:
        print("\n=================================")
        print("   SISTEMA DE GESTÃO DE BIBLIOTECA")
        print("=================================")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Pegar Empréstimo")
        print("5. Devolver Livro")
        print("6. Ver Estatísticas do Acervo (Extra)")
        print("7. Remover Livro (Extra)")
        print("0. Sair")
        print("=================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            emprestar_livro()
        elif opcao == "5":
            devolver_livro()
        elif opcao == "6":
            exibir_estatisticas()
        elif opcao == "7":
            remover_livro()
        elif opcao == "0":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida! Digite um número válido do menu.")


if __name__ == "__main__":
    menu_principal()
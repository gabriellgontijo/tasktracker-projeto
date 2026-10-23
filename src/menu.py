"""Exibição do menu do TaskTracker e leitura da opção escolhida."""


def exibir_menu():
    print("========================================")
    print("           TASKTRACKER - MENU")
    print("========================================")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair da aplicação")
    print("========================================")


def ler_opcao():
    """Lê a opção digitada pelo usuário (sem espaços nas pontas)."""
    return input("Escolha uma opção: ").strip()

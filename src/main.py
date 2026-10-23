"""
TaskTracker - Bootcamp II (Fase 2)
Ponto de entrada da aplicação de linha de comando (CLI) para gerenciamento de tarefas.

Como executar, a partir da pasta do projeto:  python src/main.py
"""

from menu import exibir_menu, ler_opcao
from tarefas import cadastrar_tarefa, concluir_tarefa, remover_tarefa, visualizar_tarefas


def main():
    """Loop principal: mostra o menu até o usuário escolher sair."""
    while True:
        exibir_menu()
        opcao = ler_opcao()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção de 1 a 5.\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C (ou fim da entrada) fecha o programa sem mostrar mensagem de erro.
        print("\n\nEncerrando o TaskTracker. Até logo!")

"""
Tarefas do TaskTracker: cadastro e listagem.

Versão inicial: cadastro e listagem básicos, ainda sem validar os dados digitados.
As regras de validação planejadas na Fase 1 entram no próximo commit.
"""

# Lista com todas as tarefas cadastradas. Cada tarefa é um dicionário.
lista_tarefas = []

# Número que identifica a próxima tarefa cadastrada (1, 2, 3...).
proximo_id = 1


# ---------------------------------------------------------------------------
# Cadastro e listagem
# ---------------------------------------------------------------------------

def cadastrar_tarefa():
    """Cadastra uma nova tarefa (ainda sem validar os dados digitados)."""
    global proximo_id
    print("\n--- Cadastro de Nova Tarefa ---")

    titulo = input("Título da tarefa: ").strip()
    descricao = input("Descrição da tarefa (opcional): ").strip()
    prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",  # toda tarefa nasce como Pendente
    }
    lista_tarefas.append(tarefa)
    proximo_id += 1

    print(f"\nTarefa #{tarefa['id']} '{titulo}' cadastrada com sucesso!\n")


def visualizar_tarefas():
    """Mostra todas as tarefas cadastradas."""
    print("\n--- Lista de Tarefas ---")

    if len(lista_tarefas) == 0:
        print("Não existem tarefas cadastradas no momento.\n")
        return

    for tarefa in lista_tarefas:
        descricao = tarefa["descricao"] if tarefa["descricao"] else "(sem descrição)"
        print(f"\nTarefa #{tarefa['id']}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {descricao}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")
    print()

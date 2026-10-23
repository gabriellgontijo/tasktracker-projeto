"""
Tarefas do TaskTracker: cadastro (com as validações) e listagem.

Segue a receita lógica e as regras planejadas na Fase 1:
- o título é obrigatório (vazio ou só espaços é recusado);
- a prioridade aceita apenas Alta, Média (ou Media) e Baixa;
- a data limite usa o formato DD/MM/AAAA e não pode ser anterior a hoje;
- toda tarefa nasce com o status "Pendente".
"""

from datetime import date, datetime

# Lista com todas as tarefas cadastradas. Cada tarefa é um dicionário.
lista_tarefas = []

# Prioridades aceitas, na ordem em que aparecem na listagem.
PRIORIDADES_VALIDAS = ["Alta", "Média", "Baixa"]

# Número que identifica a próxima tarefa cadastrada (1, 2, 3...).
proximo_id = 1


# ---------------------------------------------------------------------------
# Validação das entradas
# ---------------------------------------------------------------------------

def ler_titulo():
    """Pede o título até o usuário digitar algo que não seja vazio."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo != "":
            return titulo
        print("Erro: o título não pode ficar vazio. Digite novamente.")


def ler_prioridade():
    """Pede a prioridade até o usuário digitar Alta, Média (ou Media) ou Baixa."""
    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip().capitalize()
        if prioridade == "Media":
            prioridade = "Média"
        if prioridade in PRIORIDADES_VALIDAS:
            return prioridade
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def ler_data_limite():
    """Pede a data limite (DD/MM/AAAA) e não aceita datas anteriores a hoje."""
    while True:
        texto = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            print("Erro: data inválida. Use o formato DD/MM/AAAA (exemplo: 31/12/2026).")
            continue
        if data < date.today():
            print("Erro: a data limite não pode ser anterior à data de hoje.")
            continue
        return data.strftime("%d/%m/%Y")


# ---------------------------------------------------------------------------
# Cadastro e listagem
# ---------------------------------------------------------------------------

def cadastrar_tarefa():
    """Cadastra uma nova tarefa seguindo o passo a passo da Fase 1."""
    global proximo_id
    print("\n--- Cadastro de Nova Tarefa ---")

    titulo = ler_titulo()
    descricao = input("Descrição da tarefa (opcional): ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()

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

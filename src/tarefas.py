"""
Tarefas do TaskTracker: cadastro (com as validações), listagem, conclusão e remoção.

Segue a receita lógica e as regras planejadas na Fase 1:
- o título é obrigatório (vazio ou só espaços é recusado);
- a prioridade aceita apenas Alta, Média (ou Media) e Baixa;
- a data limite usa o formato DD/MM/AAAA e não pode ser anterior a hoje;
- toda tarefa nasce com o status "Pendente";
- a listagem mostra primeiro Alta, depois Média, depois Baixa, com os totais;
- só é possível concluir ou remover uma tarefa que exista na lista.
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


def posicao_da_prioridade(tarefa):
    """Usada na ordenação: Alta vem primeiro, depois Média, depois Baixa."""
    return PRIORIDADES_VALIDAS.index(tarefa["prioridade"])


def visualizar_tarefas():
    """Mostra as tarefas ordenadas por prioridade e um resumo no final."""
    print("\n--- Lista de Tarefas ---")

    if len(lista_tarefas) == 0:
        print("Não existem tarefas cadastradas no momento.\n")
        return

    for tarefa in sorted(lista_tarefas, key=posicao_da_prioridade):
        descricao = tarefa["descricao"] if tarefa["descricao"] else "(sem descrição)"
        print(f"\nTarefa #{tarefa['id']}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {descricao}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")

    pendentes = 0
    concluidas = 0
    for tarefa in lista_tarefas:
        if tarefa["status"] == "Pendente":
            pendentes += 1
        elif tarefa["status"] == "Concluída":
            concluidas += 1

    print(f"\nTotal: {len(lista_tarefas)} tarefa(s) | Pendentes: {pendentes} | Concluídas: {concluidas}\n")


# ---------------------------------------------------------------------------
# Conclusão e remoção
# ---------------------------------------------------------------------------

def buscar_tarefa(identificacao):
    """Procura a tarefa pelo número (#) ou pelo título. Devolve None se não achar."""
    if identificacao.isdigit():
        for tarefa in lista_tarefas:
            if tarefa["id"] == int(identificacao):
                return tarefa
    for tarefa in lista_tarefas:
        if tarefa["titulo"].lower() == identificacao.lower():
            return tarefa
    return None


def concluir_tarefa():
    """Marca uma tarefa existente como Concluída."""
    print("\n--- Concluir Tarefa ---")

    if len(lista_tarefas) == 0:
        print("Não existem tarefas cadastradas no momento.\n")
        return

    identificacao = input("Número ou título da tarefa: ").strip()
    tarefa = buscar_tarefa(identificacao)

    if tarefa is None:
        print("Erro: tarefa não encontrada.\n")
    elif tarefa["status"] == "Concluída":
        print(f"A tarefa #{tarefa['id']} já estava concluída.\n")
    else:
        tarefa["status"] = "Concluída"
        print(f"Tarefa #{tarefa['id']} '{tarefa['titulo']}' marcada como concluída!\n")


def remover_tarefa():
    """Remove da lista uma tarefa existente."""
    print("\n--- Remover Tarefa ---")

    if len(lista_tarefas) == 0:
        print("Não existem tarefas cadastradas no momento.\n")
        return

    identificacao = input("Número ou título da tarefa: ").strip()
    tarefa = buscar_tarefa(identificacao)

    if tarefa is None:
        print("Erro: tarefa não encontrada.\n")
    else:
        lista_tarefas.remove(tarefa)
        print(f"Tarefa #{tarefa['id']} '{tarefa['titulo']}' removida.\n")

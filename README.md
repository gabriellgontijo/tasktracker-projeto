# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastrar, organizar e acompanhar tarefas do dia a dia.
Projeto do **Bootcamp II**, desenvolvido de forma cumulativa a partir do planejamento lógico da Fase 1
(disponível em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf)).

## Funcionalidades

Menu contínuo com cinco opções:

1. **Cadastrar nova tarefa** — título, descrição, prioridade e data limite, com validação dos dados.
2. **Visualizar tarefas cadastradas** — lista organizada por prioridade (Alta, depois Média, depois Baixa), com o total de tarefas pendentes e concluídas.
3. **Concluir tarefa** — muda o status da tarefa para Concluída.
4. **Remover tarefa** — tira a tarefa da lista.
5. **Sair da aplicação.**

Cada tarefa recebe um número (#1, #2, #3...) que pode ser usado para concluí-la ou removê-la. Quando ainda não existe nenhuma tarefa, o sistema avisa com uma mensagem clara.

## Regras de negócio (validações)

| Campo / ação | Regra |
|---|---|
| Título | Obrigatório. Entrada vazia ou só com espaços é recusada e o sistema pede de novo. |
| Descrição | Texto livre e opcional. |
| Prioridade | Aceita apenas **Alta**, **Média** (ou Media) e **Baixa**, sem diferenciar maiúsculas. Outro valor gera erro e nova digitação. |
| Data limite | Formato DD/MM/AAAA. Datas inexistentes ou anteriores a hoje são recusadas. |
| Status | Definido automaticamente como **Pendente** no cadastro. |
| Concluir / remover | Só funciona para uma tarefa que exista na lista (busca pelo número ou pelo título). |

## Tecnologias utilizadas

- **Python 3** — apenas a biblioteca padrão; nenhuma instalação extra é necessária.
- **Git** e **GitHub** — controle de versão e publicação do projeto.

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                    # Este arquivo
├── .gitignore                   # Arquivos temporários do Python e ambientes virtuais
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico entregue na Fase 1
├── src/
│   ├── main.py                  # Ponto de entrada: loop principal do menu
│   ├── tarefas.py               # Cadastro, validações, listagem, conclusão e remoção
│   └── menu.py                  # Exibição do menu e leitura da opção
└── requirements.txt             # Dependências (nenhuma: só biblioteca padrão)
```

## Como instalar e executar

1. Instale o **Python 3** pelo site [python.org/downloads](https://www.python.org/downloads/).
   No Windows, marque a opção **"Add python.exe to PATH"** durante a instalação.
2. Baixe o projeto: clique no botão verde **Code**, copie a URL e rode:
   ```
   git clone <URL-do-repositório>
   cd tasktracker-projeto
   ```
3. Execute a aplicação:
   ```
   python src/main.py
   ```
   No Windows, se o comando `python` não for reconhecido, use `py src/main.py`.

Não é preciso instalar nada do `requirements.txt`: o projeto usa só a biblioteca padrão do Python.

## Exemplo de uso

```
========================================
           TASKTRACKER - MENU
========================================
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Concluir tarefa
4. Remover tarefa
5. Sair da aplicação
========================================
Escolha uma opção: 1

--- Cadastro de Nova Tarefa ---
Título da tarefa:
Erro: o título não pode ficar vazio. Digite novamente.
Título da tarefa: Entregar a Fase 2 do Bootcamp
Descrição da tarefa (opcional): Repositório, Colab e vídeo
Prioridade (Alta, Média ou Baixa): Urgente
Erro: prioridade inválida. Digite Alta, Média ou Baixa.
Prioridade (Alta, Média ou Baixa): Alta
Data limite (DD/MM/AAAA): 31/10/2026

Tarefa #1 'Entregar a Fase 2 do Bootcamp' cadastrada com sucesso!
```

## Evolução do projeto

- **Fase 1 — Planejamento lógico:** entendimento do problema, entradas, saídas, regras e algoritmo em português. *(concluída)*
- **Fase 2 — Versionamento e implementação:** repositório no GitHub e aplicação em Python com as regras de negócio. *(esta etapa)*
- **Fase 3 — Containerização:** empacotar a aplicação com Docker. *(próxima etapa)*

## Autor

**Gabriel Lagares Gontijo**
Ciência de Dados · Bootcamp II — CEUB EAD

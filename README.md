# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastrar, organizar e acompanhar tarefas, empacotada em um container Docker.
Projeto do **Bootcamp II**, construído em três fases a partir do planejamento lógico da Fase 1
(disponível em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf)).

## Como executar com Docker

**Pré-requisito:** Docker instalado — Docker Desktop no Windows ou no macOS, Docker Engine no Linux.
Abra o terminal na pasta do projeto e use os comandos abaixo.

**Como construir a imagem:**

```bash
docker build -t tasktracker .
```

**Como rodar o container em modo isolado:**

```bash
docker run -it --rm tasktracker
```

**Como rodar via orquestração (Recomendado):**

```bash
docker compose run --rm tasktracker-app
```

### O que cada parte dos comandos faz

| Trecho | Função |
|---|---|
| `-t tasktracker` (no build) | Dá o nome `tasktracker` à imagem criada a partir do `Dockerfile`. |
| `-it` | `-i` mantém a entrada de dados aberta e `-t` cria um terminal. Sem isso o menu não consegue ler o que você digita. |
| `--rm` | Apaga o container quando você sai do programa, sem deixar sobras. |
| `docker compose run` | Lê o `docker-compose.yml`, que já traz `stdin_open: true` e `tty: true` (o equivalente ao `-it`), e constrói a imagem sozinho se ela ainda não existir. |

O `docker compose run` é o recomendado para esta aplicação: o `docker compose up` foi pensado para serviços que rodam em segundo plano e não conecta o teclado ao container, enquanto o `run` liga o seu terminal ao menu interativo.

### Rodar sem Docker (opcional)

Com o Python 3 instalado:

```bash
python src/main.py
```

## Decisões técnicas do Dockerfile

| Instrução | Por quê |
|---|---|
| `FROM python:3.11-slim` | Imagem oficial e enxuta do Python 3.11: tem só o necessário, então baixa e inicia rápido. |
| `WORKDIR /app` | Define a pasta de trabalho dentro do container. |
| `ENV PYTHONUNBUFFERED=1` | Mostra a saída do programa na hora, sem atraso de buffer — importante numa aplicação interativa. |
| `ENV PYTHONDONTWRITEBYTECODE=1` | Evita gerar arquivos `.pyc` dentro do container. |
| `COPY src/ /app/src/` | Copia só o código da aplicação. O `.dockerignore` deixa de fora `.git`, `docs` e caches do Python. |
| Sem `pip install` | O projeto usa apenas a biblioteca padrão do Python, por isso a imagem fica leve e o build é rápido. |
| `RUN useradd` + `USER appuser` | A aplicação roda com um usuário comum, sem privilégios de administrador (boa prática de segurança). |
| `CMD ["python", "src/main.py"]` | Comando que abre o menu do TaskTracker quando o container inicia. |

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

- **Python 3.11** — apenas a biblioteca padrão.
- **Docker** e **Docker Compose** — empacotamento e execução da aplicação em container.
- **Git** e **GitHub** — versionamento e publicação do projeto.

## Estrutura do repositório

```
tasktracker-projeto/
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico da Fase 1 (rastreabilidade)
├── src/
│   ├── main.py                  # Ponto de entrada: loop principal do menu
│   ├── tarefas.py               # Cadastro, validações, listagem, conclusão e remoção
│   └── menu.py                  # Exibição do menu e leitura da opção
├── .dockerignore                # O que fica fora do build da imagem
├── .gitignore                   # Arquivos temporários do Python e ambientes virtuais
├── Dockerfile                   # Receita da imagem da aplicação
├── docker-compose.yml           # Orquestração da execução interativa
├── requirements.txt             # Dependências (nenhuma: só biblioteca padrão)
└── README.md                    # Este arquivo
```

## Exemplo de uso

```
$ docker compose run --rm tasktracker-app
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
Título da tarefa: Entregar a Fase 3 do Bootcamp
Descrição da tarefa (opcional): Dockerfile, compose e vídeo
Prioridade (Alta, Média ou Baixa): Urgente
Erro: prioridade inválida. Digite Alta, Média ou Baixa.
Prioridade (Alta, Média ou Baixa): Alta
Data limite (DD/MM/AAAA): 31/12/2026

Tarefa #1 'Entregar a Fase 3 do Bootcamp' cadastrada com sucesso!
```

## Evolução do projeto

- **Fase 1 — Planejamento lógico:** entendimento do problema, entradas, saídas, regras e algoritmo em português. *(concluída)*
- **Fase 2 — Versionamento e implementação:** repositório no GitHub e aplicação em Python com as regras de negócio. *(concluída)*
- **Fase 3 — Conteinerização e orquestração:** `Dockerfile`, `docker-compose.yml` e documentação para rodar a aplicação do mesmo jeito em qualquer ambiente. *(concluída)*

## Autor

**Gabriel Lagares Gontijo**
Ciência de Dados · Bootcamp II — CEUB EAD

# Imagem base oficial do Python 3.11 na versão "slim": só o essencial, bem mais leve
FROM python:3.11-slim

# Pasta de trabalho dentro do container: todos os comandos rodam a partir daqui
WORKDIR /app

# PYTHONUNBUFFERED=1 mostra as mensagens do programa na hora, sem ficar em buffer
# PYTHONDONTWRITEBYTECODE=1 evita criar arquivos .pyc dentro do container
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Copia o código da aplicação (src/) para dentro da imagem.
# Não há "pip install": o TaskTracker usa só a biblioteca padrão do Python.
COPY src/ /app/src/

# Segurança: a aplicação roda com um usuário comum, sem privilégios de administrador
RUN useradd --create-home appuser
USER appuser

# Comando executado quando o container inicia: abre o menu do TaskTracker
CMD ["python", "src/main.py"]

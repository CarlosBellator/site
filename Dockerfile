# Dockerfile otimizado para deploy Django no Cloud Run
FROM python:3.11-slim

# Dependências do sistema (adapte se precisar de libs extras)
RUN apt-get update && apt-get install -y build-essential gcc libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia only requirements first para aproveitar cache do Docker
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia código da aplicação
COPY . /app

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Cria diretório para staticfiles coletados
RUN mkdir -p /app/staticfiles

# Comando padrão (Cloud Run usa $PORT)
CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8080", "--workers", "2"]
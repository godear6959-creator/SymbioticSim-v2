# Usar una imagen de Python ligera
FROM python:3.11-slim

# Evitar que Python genere archivos .pyc y habilitar logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para Matplotlib
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto
COPY . .

# Crear carpeta para guardar los resultados de la simulación
RUN mkdir -p output

# Comando por defecto: ejecutar la simulación
CMD ["python", "src/symbiotic_sim.py"]

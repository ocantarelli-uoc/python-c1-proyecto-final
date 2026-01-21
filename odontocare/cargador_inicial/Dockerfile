FROM python:3.14-alpine
# Directorio de trabajo
WORKDIR /app
# Instala dependencias
COPY ./cargador_inicial/requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt
# Comando para ejecutar la app
CMD ["python", "run.py"]  
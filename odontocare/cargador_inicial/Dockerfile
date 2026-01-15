FROM python:3.9-alpine
# Directorio de trabajo
WORKDIR /app
# Instala dependencias
COPY ./cargador_inicial/requirements.txt .  
RUN pip install -r requirements.txt
# Copia la aplicación
# Comando para ejecutar la app
CMD ["python", "run.py"]  
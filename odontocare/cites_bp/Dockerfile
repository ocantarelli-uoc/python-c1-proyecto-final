FROM python:3.9-alpine
# Directorio de trabajo
WORKDIR /app
# Instala dependencias
COPY requirements.txt .  
RUN pip install -r requirements.txt
# Copia la aplicación
COPY . .
# Expone el puerto 5001
EXPOSE 5002
# Comando para ejecutar la app
CMD ["python", "run.py"]  
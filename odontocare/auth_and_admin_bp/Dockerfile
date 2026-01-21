FROM python:3.14-alpine
# Directorio de trabajo
WORKDIR /app
# Instala dependencias
COPY ./auth_and_admin_bp/requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache curl
# Expone el puerto 5001
EXPOSE 5001
# Comando para ejecutar la app
CMD ["python", "run.py"]  
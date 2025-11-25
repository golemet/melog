# Usar una imagen base de Python 3.10 slim
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que se ejecuta la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "app.py"]

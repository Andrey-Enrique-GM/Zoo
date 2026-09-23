# Imagen base con Python 3.14
FROM python:3.14

# Carpetas de trabajo dentro del contenedor para nuestra aplicacion zoo
WORKDIR /app

# Copia archivos desde mi proyecto hacia la imagen que estoy construyendo.
# El primer punto (.) representa el directorio actual de mi proyecto, que es el origen.
# El segundo punto (.) representa el directorio actual dentro de la imagen, que es el destino.
# Se usa . porque ambos representan el directorio actual segun el contexto de cada lado.
COPY . .


# Instalar las dependencias de Python
RUN pip install -r requirements.txt

# Comando que se ejecutara al iniciar el contenedor
CMD [ "python", "app.py" ]
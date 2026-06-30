en la cmd dentro de la carpeta backend cree una burbuja (entorno virtual) con el comando 

python -m venv venv

luego active la burbuja

venv\Scripts\activate

instale las herramientas

pip install fastapi uvicorn pymongo python-dotenv

--

Para que sirve el venv?

Imaginemos el compu como la cocina, si instalo las librerias directamente se mezclaria todo con proyectos futuros y la comida se contaminaria 

el venv (Virtual environment) es como un tupper cerrado explusivo para esta comidita, todo lo que instalemos queda ahi y no afecta el resto del pc 

--

Compañeros importante que en su pc agreguen dentro de la carpeta proyecto_restaurant un archivo llamado .gitignore para que no se suba al github el archivo venv (que esta dentro de la carpeta backend) y si quieren crear un archivo .env(tambien dentro de la carpeta backend) donde guarden las contraseñas y links importantes igual lo ponen en el gitignore con este comando 

# Ignorar entornos virtuales
backend/venv/

# Ignorar archivos secretos
backend/.env


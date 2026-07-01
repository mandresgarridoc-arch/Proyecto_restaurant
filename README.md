Hola equipo recordatorio para poder trabajar un repositorio compartido.

1-. Si el repositorio no esta en nuestro pc primero debemos crear una copia del repositorio en nuestro pc, 
para esto primero debemos ir a la carpeta donde crearemos al copia, ej: C:/ 


Stack Tecnológico
Frontend: React, TypeScript, Tailwind CSS.

Backend: Python, FastAPI.

Base de Datos: MongoDB (NoSQL) alojado en MongoDB Atlas.

Infraestructura: Despliegue en la nube (Vercel y Render).

Bitácora de Desarrollo (Progreso Actual)
A continuación, se detalla el progreso del proyecto organizado por hitos técnicos:

Sprint 1: Infraestructura y Base NoSQL
Configuración del Monorepo: Estructura inicial del repositorio dividida en /backend y /frontend.

Documentación Inicial: Elaboración del diagnóstico técnico, requerimientos funcionales y no funcionales (Capítulo 1 del Informe Técnico).

Entorno de Desarrollo:

Configuración de entornos virtuales de Python (venv).

Configuración de React con TypeScript y Tailwind CSS.

Implementación de .gitignore para seguridad (protección de .env y carpetas de dependencias).

Diseño de Base de Datos: Definición del modelo documental en MongoDB (mesas, carta, pedidos) con enfoque en subdocumentos embebidos.

Cómo ejecutar el proyecto en modo desarrollo
Requisitos previos
Tener instalado Node.js (versión LTS).

Tener instalado Python.

Backend
Bash
cd backend
# Activar entorno virtual
venv\Scripts\activate  # En Windows
# Instalar dependencias
pip install fastapi uvicorn pymongo python-dotenv
# Iniciar servidor
uvicorn main:app --reload
Frontend
Bash
cd frontend
# Instalar dependencias
npm install
# Iniciar servidor
npm run dev
🔒 Nota de Seguridad
Este proyecto utiliza variables de entorno (.env) para la conexión a la base de datos. Por razones de seguridad, este archivo no está incluido en el repositorio. Asegúrese de configurar sus propias credenciales de MongoDB Atlas en el archivo local para realizar pruebas.

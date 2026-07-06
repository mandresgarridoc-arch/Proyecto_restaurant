Hola equipo recordatorio para poder trabajar un repositorio compartido.

1-. En cmd ir a direccion de proyecto y ejecutar git clone 
2.- En ubicacion de proyecto escribir el comando git status para revisar si hay cambios a medias
3.- Descargar los cambios con 

Proyecto: Sistema de Gestión Gastronómica "RestoManager"
Este repositorio contiene el desarrollo del sistema de gestión para un restaurante, realizado como proyecto integrador para la asignatura de Bases de Datos No Estructuradas.

Stack Tecnológico
Frontend: React, TypeScript, Tailwind CSS.

Backend: Python, FastAPI.

Base de Datos: MongoDB (NoSQL) alojado en MongoDB Atlas.

Infraestructura: Despliegue en la nube (Vercel y Render).

Bitácora de Desarrollo (Progreso Actual) 30-06-2026
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
Nota de Seguridad
Este proyecto utiliza variables de entorno (.env) para la conexión a la base de datos. Por razones de seguridad, este archivo no está incluido en el repositorio. Asegúrese de configurar sus propias credenciales de MongoDB Atlas en el archivo local para realizar pruebas.


Bitácora: Configuración del Backend
Hemos implementado la base del servidor con FastAPI y configurado la conexión a MongoDB Atlas mediante variables de entorno.

Guía Rápida para el equipo:
Activar el Entorno Virtual (siempre primero):

Bash
cd backend
venv\Scripts\activate
Probar la API (Local):

Bash
uvicorn main:app --reload
Una vez corriendo, abre http://127.0.0.1:8000/docs para verificar los endpoints y probar la conexión con la base de datos de forma interactiva.

Requisito: Asegúrate de tener el archivo .env en la carpeta /backend con tu MONGO_URI.
(Nota: Este archivo es privado y no se subirá al repositorio por seguridad).

IMPORTANTE RECORDAR:
Si el comando uvicorn falla: Asegúrate siempre de ver el (venv) al inicio de tu terminal. Si no está, ejecutan el comando de activación nuevamente.

Si hay error de conexión: Revisen que su IP esté autorizada en el panel de Network Access de MongoDB Atlas.
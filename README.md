## Backend - FastAPI

API REST desarrollada con FastAPI que consume datos de StackExchange y realiza consultas SQL sobre vuelos en México.
El proyecto está completamente dockerizado y listo para ejecutarse fácilmente.

## Requisitos previos
Docker instalado  
Docker Compose instalado  
Docker Desktop en ejecución 


## Configuración de red (obligatorio)

Antes de levantar los contenedores, es necesario crear la red de Docker que permitirá la comunicación entre backend y frontend.

Abrir una terminal en la raíz del proyecto backend y ejecutar:

    docker network create reto-network

Este paso se realiza una sola vez.


## Tecnologías
FastAPI  
PostgreSQL  
Docker 


## Ejecución

1. Abrir una terminal en la carpeta raíz del proyecto (donde se encuentra el archivo docker-compose.yml)

2. Ejecutar:

    docker-compose up --build

3. Esperar a que los contenedores se levanten correctamente



## Accesos
    * API: http://localhost:8000
    * Swagger: http://localhost:8000/docs


## Base de datos
La base de datos PostgreSQL se inicializa automáticamente mediante el archivo init.sql, el cual incluye:

- Creación de tablas
- Inserción de datos


## Endpoints
StackExchange
GET /stack/answered        -> Respuestas contestadas vs no contestadas
GET /stack/max-reputation  -> Mayor reputación
GET /stack/min-views       -> Menor número de vistas
GET /stack/oldest          -> Pregunta más antigua
GET /stack/newest          -> Pregunta más reciente

Vuelos
GET /vuelos/top-aeropuerto     -> Aeropuerto(s) con mayor movimiento
GET /vuelos/top-aerolinea      -> Aerolínea(s) con más vuelos
GET /vuelos/top-dia            -> Día(s) con más vuelos
GET /vuelos/aerolineas-mas-2   -> Aerolíneas con más de 2 vuelos por día


## Notas
Se utiliza una red externa de Docker (reto-network) para la comunicación entre servicios  
Se manejan empates en consultas, por lo que pueden devolverse múltiples resultados  
Se manejan casos sin resultados con mensajes claros  
Arquitectura organizada en routes y services  
El backend expone el servicio en http://localhost:8000 para su consumo

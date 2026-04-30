## Backend - FastAPI

API REST desarrollada con FastAPI que consume datos de StackExchange y realiza consultas SQL sobre vuelos en México.
El proyecto está completamente dockerizado y listo para ejecutarse en cualquier entorno.


## Requisitos previos
Docker instalado  
Docker Compose instalado  
Docker Desktop en ejecución 


## Tecnologías
FastAPI                     -> Framework principal 
PostgreSQL                  -> Base de datos
Docker + Docker Compose     -> Contenedorización
pytest                      -> Pruebas unitarias
Swagger                     -> Documentación automática


## Instalación y ejecución

### 1. Crear la red Doker
Antes de levantar los contenedores, es necesario crear la red de Docker que permitirá la comunicación entre backend y frontend.

Abrir una terminal en la raíz del proyecto backend y ejecutar:

    docker network create reto-network

Este paso se realiza una sola vez.


### 2. Levantar los contenedores
1. En una terminal en la carpeta raíz del proyecto (donde se encuentra el archivo docker-compose.yml)

2. Ejecutar:

    docker-compose up --build

3. Esperar a que los contenedores se levanten correctamente


### 3. Verificar que todo esté corriendo

    docker ps

## Accesos
    * API: http://localhost:8000
    * Swagger: http://localhost:8000/docs


## Base de datos

PostgreSQL se inicializa automáticamente al levantar los contenedores mediante 'init.sql', que incluye:

- Creación de tablas: 'aerolineas', 'aeropuertos', 'movimientos', 'vuelos'
- Inserción de datos de ejemplo

No se requiere ninguna configuración manual.


## Pruebas unitarias

Los tests cubren todos los servicios (StackExchange y Vuelos) con 10 casos de prueba.
Abrir una terminal en la raíz del proyecto y ejecutar:

# Correr tests
    docker exec -it backend pytest app/tests/ -v

# Con reporte de cobertura
    docker exec -it backend pytest app/tests/ --cov=app/services --cov-report=term-missing



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

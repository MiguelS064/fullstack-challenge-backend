-- Creación de tablas
CREATE TABLE aerolineas (
  id_aerolinea INT,
  nombre_aerolinea VARCHAR(50)
);

CREATE TABLE aeropuertos (
  id_aeropuerto INT,
  nombre_aeropuerto VARCHAR(50)
);

CREATE TABLE movimientos (
  id_movimiento INT,
  descripcion VARCHAR(50)
);

CREATE TABLE vuelos (
  id_aerolinea INT,
  id_aeropuerto INT,
  id_movimiento INT,
  dia DATE
);

-- Insertar Aerolíneas
INSERT INTO aerolineas (id_aerolinea, nombre_aerolinea) VALUES 
(1, 'Volaris'), 
(2, 'Aeromar'), 
(3, 'Interjet'), 
(4, 'Aeromexico');

-- Insertar Aeropuertos
INSERT INTO aeropuertos (id_aeropuerto, nombre_aeropuerto) VALUES 
(1, 'Benito Juarez'), 
(2, 'Guanajuato'), 
(3, 'La paz'), 
(4, 'Oaxaca');

-- Insertar Movimientos
INSERT INTO movimientos (id_movimiento, descripcion) VALUES 
(1, 'Salida'), 
(2, 'Llegada');

-- Insertar Vuelos
INSERT INTO vuelos (id_aerolinea, id_aeropuerto, id_movimiento, dia) VALUES 
(1, 1, 1, '2021-05-02'), 
(2, 1, 1, '2021-05-02'),
(3, 2, 2, '2021-05-02'), 
(4, 3, 2, '2021-05-02'), 
(1, 3, 2, '2021-05-02'),
(2, 1, 1, '2021-05-02'), 
(2, 3, 1, '2021-05-04'), 
(3, 4, 1, '2021-05-04'),
(3, 4, 1, '2021-05-04');

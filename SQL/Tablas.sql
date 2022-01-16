CREATE DATABASE IF NOT EXISTS soriano_malo_final;
USE soriano_malo_final;

/* Tablas Soriano_Malo_Final */

CREATE TABLE usuario(
    cedula VARCHAR(10) NOT NULL PRIMARY KEY,
    nombre VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL UNIQUE,
    contrasenia VARCHAR(40) NOT NULL
);

CREATE TABLE encuesta(
    id_encuesta INTEGER UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(60) NOT NULL,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    cedula VARCHAR(10) NOT NULL,

    FOREIGN KEY (cedula) REFERENCES usuario(cedula),
    UNIQUE(titulo, cedula)
);

CREATE TABLE cerrada(
    pos_pregunta INTEGER UNSIGNED NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    enunciado VARCHAR(80) NOT NULL,
    seleccionar_varias BOOLEAN NOT NULL DEFAULT False,

    PRIMARY KEY (pos_pregunta, id_encuesta),
    FOREIGN KEY (id_encuesta) REFERENCES encuesta(id_encuesta)
);

CREATE TABLE abierta(
    pos_pregunta INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    enunciado VARCHAR(80) NOT NULL,

    PRIMARY KEY (pos_pregunta, id_encuesta),
    FOREIGN KEY (id_encuesta) REFERENCES encuesta(id_encuesta)
);

CREATE TABLE opcion(
    pos_opcion INTEGER UNSIGNED NOT NULL,
    pos_pregunta INTEGER UNSIGNED NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    enunciado VARCHAR(80) NOT NULL,

    PRIMARY KEY (pos_opcion, pos_pregunta, id_encuesta),
    FOREIGN KEY (pos_pregunta, id_encuesta) REFERENCES cerrada(pos_pregunta, id_encuesta)
);

/* Tablas de Relacion */

CREATE TABLE escoge_opcion(
    cedula VARCHAR(10) NOT NULL,
    pos_opcion INTEGER UNSIGNED NOT NULL,
    pos_pregunta INTEGER UNSIGNED NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    respuesta TEXT,

    FOREIGN KEY (cedula) REFERENCES usuario(cedula),
    FOREIGN KEY (pos_opcion, pos_pregunta, id_encuesta) REFERENCES opcion(pos_opcion, pos_pregunta, id_encuesta),
    UNIQUE(cedula, pos_opcion, pos_pregunta, id_encuesta)
);

CREATE TABLE responde_abierta(
    cedula VARCHAR(10) NOT NULL,
    pos_pregunta INTEGER UNSIGNED NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    respuesta TEXT,

    FOREIGN KEY (cedula) REFERENCES usuario(cedula),
    FOREIGN KEY (pos_pregunta, id_encuesta) REFERENCES abierta(pos_pregunta, id_encuesta),
    UNIQUE(cedula, pos_pregunta, id_encuesta)
);

/* Notas
    SELECT LAST_INSERT_ID();
*/

/*Datos de Prueba*/

INSERT INTO usuario(cedula, nombre, email, contrasenia) VALUES 
    ('1720688918', 'Mario Casta', 'mario@u.com', SHA1('mario')),
    ('1720688900', 'Juana De Arcos', 'juana@u.com', SHA1('juana'));

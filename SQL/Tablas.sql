CREATE DATABASE IF NOT EXISTS soriano_malo_final;
USE soriano_malo_final;

/* Tablas Soriano_Malo_Final */

CREATE TABLE usuario(
    id_usuario INTEGER UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(40) NOT NULL,
    usuario VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL UNIQUE,
    contrasenia VARCHAR(40) NOT NULL
);

CREATE TABLE encuesta(
    id_encuesta INTEGER UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(60) NOT NULL,
    fehca TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_usuario INTEGER UNSIGNED NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    UNIQUE(titulo, id_usuario)
);

CREATE TABLE cerrada(
    id_pregunta INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    pregunta VARCHAR(60) NOT NULL,
    seleccionar_varias BOOLEAN NOT NULL DEFAULT False,
    PRIMARY KEY (id_pregunta, id_encuesta),
    FOREIGN KEY (id_encuesta) REFERENCES encuesta(id_encuesta)
);

CREATE TABLE abierta(
    id_pregunta INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    pregunta VARCHAR(60) NOT NULL,
    PRIMARY KEY (id_pregunta, id_encuesta),
    FOREIGN KEY (id_encuesta) REFERENCES encuesta(id_encuesta)
);

/* Atributo multivalorado Opcion de Cerrada */

CREATE TABLE opcion(
    id_pregunta INTEGER UNSIGNED NOT NULL,
    opcion VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_pregunta) REFERENCES cerrada(id_pregunta)
);

/* Tablas de Relacion */

CREATE TABLE responde_cerrada(
    id_usuario INTEGER UNSIGNED NOT NULL,
    id_pregunta INTEGER UNSIGNED NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    respuesta TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_pregunta, id_encuesta) REFERENCES cerrada(id_pregunta, id_encuesta)
);

CREATE TABLE responde_abierta(
    id_usuario INTEGER UNSIGNED NOT NULL,
    id_pregunta INTEGER UNSIGNED NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    respuesta TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_pregunta, id_encuesta) REFERENCES abierta(id_pregunta, id_encuesta)
);

/* Notas
    SELECT LAST_INSERT_ID();
*/

/*Datos de Prueba*/

INSERT INTO usuario(nombre, usuario, email, contrasenia) VALUES 
    ('Mario', 'Mario64', 'mario@u.com', SHA1('hola2')),
    ('Juana', 'JJ Ana', 'juana@u.com', SHA1('jjana'));

INSERT INTO encuesta(id_usuario, titulo) VALUES 
    (1, 'Probando'),
    (2, 'Encuesta');
/*Tablas Bitacoras*/

CREATE TABLE bitacora_encuesta(
    operacion VARCHAR(20) NOT NULL,
    tabla VARCHAR(20) NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    pos_pregunta INTEGER UNSIGNED,
    pos_opcion INTEGER UNSIGNED,
    cedula VARCHAR(10),
    usuario VARCHAR(30) NOT NULL,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bitacora_respuesta(
    operacion VARCHAR(20) NOT NULL,
    tabla VARCHAR(20) NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    pos_pregunta INTEGER UNSIGNED NOT NULL,
    pos_opcion INTEGER UNSIGNED,
    cedula VARCHAR(10) NOT NULL,
    usuario VARCHAR(30) NOT NULL,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

/*TRIGGERS De Bitacora de ingreso de una encuesta.*/

DELIMITER $$
CREATE TRIGGER encuesta_insert
AFTER INSERT ON encuesta
FOR EACH ROW 
BEGIN
    INSERT INTO bitacora_encuesta VALUES 
        ('INSERT', 'encuesta', NEW.id_encuesta, NULL, NULL, NEW.cedula, CURRENT_USER(), NOW());
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER abierta_insert
AFTER INSERT ON abierta
FOR EACH ROW 
BEGIN
    INSERT INTO bitacora_encuesta VALUES 
        ('INSERT', 'abierta', NEW.id_encuesta, NEW.pos_pregunta, NULL, NULL, CURRENT_USER(), NOW());
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER cerrada_insert
AFTER INSERT ON cerrada
FOR EACH ROW 
BEGIN
    INSERT INTO bitacora_encuesta VALUES 
        ('INSERT', 'cerrada', NEW.id_encuesta, NEW.pos_pregunta, NULL, NULL, CURRENT_USER(), NOW());
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER opcion_insert
AFTER INSERT ON opcion
FOR EACH ROW 
BEGIN
    INSERT INTO bitacora_encuesta VALUES 
        ('INSERT', 'opcion', NEW.id_encuesta, NEW.pos_pregunta, NEW.pos_opcion, NULL, CURRENT_USER(), NOW());
END $$
DELIMITER ;


/*TRIGGERS De Bitacora de ingreso de una respuesta.*/

DELIMITER $$
CREATE TRIGGER responde_abierta_insert
AFTER INSERT ON responde_abierta
FOR EACH ROW 
BEGIN
    INSERT INTO bitacora_respuesta VALUES 
        ('INSERT', 'responde_abierta', NEW.id_encuesta, NEW.pos_pregunta, NULL, NEW.cedula, CURRENT_USER(), NOW());
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER escoge_opcion_insert
AFTER INSERT ON escoge_opcion
FOR EACH ROW 
BEGIN
    INSERT INTO bitacora_respuesta VALUES 
        ('INSERT', 'escoge_opcion', NEW.id_encuesta, NEW.pos_pregunta, NEW.pos_opcion, NEW.cedula, CURRENT_USER(), NOW());
END $$
DELIMITER ;
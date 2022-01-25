/*Tablas Bitacoras*/

CREATE TABLE bitacora_encuesta(
    operacion VARCHAR(20) NOT NULL,
    tabla VARCHAR(20) NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
    cedula VARCHAR(10),
    usuario VARCHAR(30) NOT NULL,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bitacora_respuesta(
    operacion VARCHAR(20) NOT NULL,
    id_encuesta INTEGER UNSIGNED NOT NULL,
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
    INSERT INTO bitacora_encuesta VALUES ('INSERT', 'encuesta', NEW.id_encuesta, NEW.cedula, SESSION_USER(), NOW());
END $$
DELIMITER ;


/*TRIGGERS De Bitacora de ingreso de una respuesta.*/

DELIMITER $$
CREATE TRIGGER responde_abierta_insert
AFTER INSERT ON responde_abierta
FOR EACH ROW 
BEGIN
    SELECT COUNT(cedula) INTO @num_a FROM responde_abierta WHERE cedula = NEW.cedula AND id_encuesta = NEW.id_encuesta;
    SELECT COUNT(cedula) INTO @num_b FROM escoge_opcion WHERE cedula = NEW.cedula AND id_encuesta = NEW.id_encuesta;
    SET @numero = @num_a + @num_b;
    IF @numero <= 1 THEN BEGIN
        INSERT INTO bitacora_respuesta VALUES ('INSERT', NEW.id_encuesta, NEW.cedula, SESSION_USER(), NOW());
    END;  END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER escoge_opcion_insert
AFTER INSERT ON escoge_opcion
FOR EACH ROW 
BEGIN
    SELECT COUNT(cedula) INTO @num_a FROM responde_abierta WHERE cedula = NEW.cedula AND id_encuesta = NEW.id_encuesta;
    SELECT COUNT(cedula) INTO @num_b FROM escoge_opcion WHERE cedula = NEW.cedula AND id_encuesta = NEW.id_encuesta;
    SET @numero = @num_a + @num_b;
    IF @numero <= 1 THEN BEGIN
        INSERT INTO bitacora_respuesta VALUES ('INSERT', NEW.id_encuesta, NEW.cedula, SESSION_USER(), NOW());
    END;  END IF;
END $$
DELIMITER ;
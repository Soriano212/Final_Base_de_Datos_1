/* Proceso para verificar cuantas encuestas*/

CREATE PROCEDURE puede_crear_encuesta(IN ced VARCHAR(10))
BEGIN
    SELECT COUNT(cedula) INTO @numero FROM encuesta WHERE cedula = ced;
    SELECT IF(@numero > 10, 0, 1);
END;

/* Proceso para verificar usuario respondio encuesta*/

CREATE PROCEDURE usuario_res_encuesta(IN ced VARCHAR(10), IN id INTEGER)
BEGIN
    SELECT COUNT(cedula) INTO @num_a FROM responde_abierta WHERE cedula = ced AND id_encuesta = id;
    SELECT COUNT(cedula) INTO @num_b FROM escoge_opcion WHERE cedula = ced AND id_encuesta = id;
    SET @numero = @num_a + @num_b;
    SELECT IF(@numero > 0, 0, 1);
END;

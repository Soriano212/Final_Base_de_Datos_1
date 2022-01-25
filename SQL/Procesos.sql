/* Proceso para verificar cuantas encuestas*/

DELIMITER $$
CREATE PROCEDURE puede_crear_encuesta(IN ced VARCHAR(10))
BEGIN
    SELECT COUNT(cedula) INTO @numero FROM encuesta WHERE cedula = ced;
    SELECT IF(@numero >= 3, 0, 1) AS Puede_crear_encuesta;
END $$
DELIMITER ;

/* Proceso para verificar usuario respondio encuesta*/

DELIMITER $$
CREATE PROCEDURE usuario_res_encuesta(IN ced VARCHAR(10), IN id INTEGER)
BEGIN
    SELECT COUNT(cedula) INTO @num_a FROM responde_abierta WHERE cedula = ced AND id_encuesta = id;
    SELECT COUNT(cedula) INTO @num_b FROM escoge_opcion WHERE cedula = ced AND id_encuesta = id;
    SET @numero = @num_a + @num_b;
    SELECT IF(@numero > 0, 1, 0) AS Usuario_ya_respondio_la_encuesta;
END $$
DELIMITER ;

/* Ver procedimientos
    show procedure status;
*/

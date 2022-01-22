/* Proceso para verificar usuario*/

CREATE PROCEDURE numEncuestaUsuario(dni in VARCHAR2) AS conn 
SYS_REFCURSOR;

BEGIN
    OPEN conn FOR --cONDICIONAL QUE IMPIDA EL INGRESO 
    SELECT count(Usuario.idUsuario) FROM Usuario
    INNER JOIN Usuario_Encuesta ON Usuario_Encuesta.id_Usuario = Usuario.idUsuario AND Usuario.idUsuario = dni
    INNER JOIN Encuesta ON Encuesta.id = Usuario_Encuesta.id_Encuesta;
    DBMS_SQL.RETURN_RESULT(conn);
END numEncuestaUsuario;
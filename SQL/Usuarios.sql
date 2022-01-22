/* Creando usuario Inicio */

CREATE USER 'inicio'@'localhost' IDENTIFIED BY 'inicio';
GRANT SELECT, INSERT ON soriano_malo_final.usuario TO 'inicio'@'localhost';
FLUSH PRIVILEGES;

/* Creando usuario encuestado */

CREATE USER 'encuestado'@'localhost' IDENTIFIED BY 'encuestado';
GRANT SELECT ON soriano_malo_final.usuario TO 'encuestado'@'localhost';
GRANT SELECT ON soriano_malo_final.encuesta TO 'encuestado'@'localhost';
GRANT SELECT ON soriano_malo_final.abierta TO 'encuestado'@'localhost';
GRANT SELECT ON soriano_malo_final.cerrada TO 'encuestado'@'localhost';
GRANT SELECT ON soriano_malo_final.opcion TO 'encuestado'@'localhost';
GRANT INSERT ON soriano_malo_final.responde_abierta TO 'encuestado'@'localhost';
GRANT INSERT ON soriano_malo_final.escoge_opcion TO 'encuestado'@'localhost';
GRANT INSERT ON soriano_malo_final.bitacora_respuesta TO 'encuestado'@'localhost';
FLUSH PRIVILEGES;

/* Creando usuario creador */

CREATE USER 'creador'@'localhost' IDENTIFIED BY 'creador';
GRANT SELECT ON soriano_malo_final.usuario TO 'creador'@'localhost';
GRANT SELECT, INSERT ON soriano_malo_final.encuesta TO 'creador'@'localhost';
GRANT SELECT, INSERT ON soriano_malo_final.abierta TO 'creador'@'localhost';
GRANT SELECT, INSERT ON soriano_malo_final.cerrada TO 'creador'@'localhost';
GRANT SELECT, INSERT ON soriano_malo_final.opcion TO 'creador'@'localhost';
GRANT INSERT ON soriano_malo_final.responde_abierta TO 'creador'@'localhost';
GRANT INSERT ON soriano_malo_final.escoge_opcion TO 'creador'@'localhost';
GRANT INSERT ON soriano_malo_final.bitacora_respuesta TO 'creador'@'localhost';
GRANT INSERT ON soriano_malo_final.bitacora_encuesta TO 'creador'@'localhost';
FLUSH PRIVILEGES;

/* Muestra privilegios */

SHOW GRANTS FOR 'encuestado'@'localhost';
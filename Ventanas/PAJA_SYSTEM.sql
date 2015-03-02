CREATE DATABASE  IF NOT EXISTS `PAJA_SYSTEM` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `PAJA_SYSTEM`;
-- MySQL dump 10.13  Distrib 5.6.19, for linux-glibc2.5 (x86_64)
--
-- Host: localhost    Database: PAJA_SYSTEM
-- ------------------------------------------------------
-- Server version	5.5.41-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Compra`
--

DROP TABLE IF EXISTS `Compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Compra` (
  `compra_id` int(11) NOT NULL,
  `compra_detalle` varchar(50) NOT NULL,
  `compra_fecha` date NOT NULL,
  `compra_gasto` decimal(10,2) NOT NULL,
  `compra_IdPersonal` int(11) NOT NULL,
  `compra_observaciones` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`compra_id`),
  KEY `compra_IdPersonal` (`compra_IdPersonal`),
  CONSTRAINT `fk_Compra_1` FOREIGN KEY (`compra_IdPersonal`) REFERENCES `Personal` (`personal_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Compra`
--

LOCK TABLES `Compra` WRITE;
/*!40000 ALTER TABLE `Compra` DISABLE KEYS */;
/*!40000 ALTER TABLE `Compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Juego`
--

DROP TABLE IF EXISTS `Juego`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Juego` (
  `juego_id` int(11) NOT NULL,
  `juego_nombre` varchar(15) DEFAULT NULL,
  `juego_imagen` varchar(200) DEFAULT NULL,
  `juego_area` varchar(15) DEFAULT NULL,
  `juego_ubicacion` varchar(50) DEFAULT NULL,
  `juego_IdPersonal` int(11) DEFAULT NULL,
  PRIMARY KEY (`juego_id`),
  KEY `juego_IdPersonal` (`juego_IdPersonal`),
  CONSTRAINT `Juego_ibfk_1` FOREIGN KEY (`juego_IdPersonal`) REFERENCES `Personal` (`personal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Juego`
--

LOCK TABLES `Juego` WRITE;
/*!40000 ALTER TABLE `Juego` DISABLE KEYS */;
INSERT INTO `Juego` VALUES (3,'Asertijos','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/search.png','Creatividad','Oficina',6),(4,'El teto','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_Image.jpeg','Psicologia','Plazoneta',6),(5,'figuras locas','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_agregar.png','Matematicas','Cuarto 3',8),(6,'Crucigramas','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/solo_cruz.png','Distraccion','Salon interno',7),(7,'Historia ','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_agregar.png','Historia','Mesa central',5),(8,'El barco','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/search.png','Juegos','Fuera',1),(9,'Elefantito','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_agregar.png','Distraccion','Interna',8),(10,'adivinanzas','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_Image.jpeg','Lenguaje','Cuarto',1),(11,'Arbol de letras','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/search.png','Aprender','Salon',10),(12,'La macarena','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_Image.jpeg','Baile','Salon de baile',9),(13,'Gravedad 10','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/search.png','holi','espol',1),(14,'Jueguito','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_agregar.png','area 51','por ahi',8),(15,'La Bamba','/home/julio/Escritorio/imagenes FB/gatoOjos.jpg','hola','atras',1);
/*!40000 ALTER TABLE `Juego` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Nino`
--

DROP TABLE IF EXISTS `Nino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Nino` (
  `nino_id` int(12) NOT NULL,
  `nino_nombre` varchar(25) NOT NULL,
  `nino_apellido` varchar(25) NOT NULL,
  `nino_edad` int(3) NOT NULL,
  `nino_esAlergico` varchar(2) NOT NULL,
  `nino_observacion` varchar(200) DEFAULT NULL,
  `nino_semillero` int(12) NOT NULL,
  PRIMARY KEY (`nino_id`),
  KEY `fk_nino_semillero_idx` (`nino_semillero`),
  CONSTRAINT `fk_nino_semillero` FOREIGN KEY (`nino_semillero`) REFERENCES `Semillero` (`semillero_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nino`
--

LOCK TABLES `Nino` WRITE;
/*!40000 ALTER TABLE `Nino` DISABLE KEYS */;
INSERT INTO `Nino` VALUES (1,'david','Zorro',3,'No','',5);
/*!40000 ALTER TABLE `Nino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Oficio`
--

DROP TABLE IF EXISTS `Oficio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Oficio` (
  `oficio_id` int(11) NOT NULL,
  `oficio_detalle` varchar(45) DEFAULT NULL,
  `oficio_destinatario` varchar(45) DEFAULT NULL,
  `oficio_estado` varchar(45) DEFAULT NULL,
  `oficio_tramite` varchar(45) DEFAULT NULL,
  `oficio_respuesta` varchar(45) DEFAULT NULL,
  `oficio_observaciones` varchar(45) DEFAULT NULL,
  `oficio_IdPersonal` int(11) NOT NULL,
  PRIMARY KEY (`oficio_id`),
  KEY `oficio_IdPersonal` (`oficio_IdPersonal`),
  CONSTRAINT `fk_Oficio_1` FOREIGN KEY (`oficio_IdPersonal`) REFERENCES `Personal` (`personal_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Oficio`
--

LOCK TABLES `Oficio` WRITE;
/*!40000 ALTER TABLE `Oficio` DISABLE KEYS */;
INSERT INTO `Oficio` VALUES (1,'hola','xhao','Recibido','909','kjk','jkj',1);
/*!40000 ALTER TABLE `Oficio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Personal`
--

DROP TABLE IF EXISTS `Personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Personal` (
  `personal_id` int(11) NOT NULL,
  `personal_nombre` varchar(25) NOT NULL,
  `personal_apellido` varchar(25) NOT NULL,
  `personal_cedula` int(10) NOT NULL,
  `personal_telefono` int(12) DEFAULT NULL,
  `personal_tipo` varchar(25) NOT NULL,
  `personal_direccion` varchar(40) NOT NULL,
  `personal_sexo` varchar(12) NOT NULL,
  `personal_correo` varchar(40) DEFAULT NULL,
  `personal_carrera` varchar(30) DEFAULT NULL,
  `personal_facultad` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`personal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Personal`
--

LOCK TABLES `Personal` WRITE;
/*!40000 ALTER TABLE `Personal` DISABLE KEYS */;
INSERT INTO `Personal` VALUES (1,'julio','realpe',49,494,'Ayudante','fjkf','Masculino','j@gmail.com','fj','jk'),(2,'Teresa','Echeverria',912345678,991837635,'Profesor','Calle Salinas','Masculino','teche@gmail.com','Ing. Marketing','FEN'),(3,'john','Cedeno',916718283,2147483647,'Personal Contratado','Mapasingue ','Masculino','jjj@gmail.com','ing. Computacion','FIEC'),(4,'Juan','Vaca',987654321,2147483647,'Voluntario','Sauces','Masculino','jjvaca@gmail.com','Ing. Computacion','FIEC'),(5,'David','Pazmino',987678768,2147483647,'Profesor','Sur','Masculino','david@gmail.com','Ing. Potencia','FIEC'),(6,'Sheila','Gallegos',987676578,987654536,'Ayudante','Duran','Femenino','shei@yahoo.com','Ing. ELectrica','FIEC'),(7,'Katty Mary','Hermenejildo de Cedeno',989878767,987678765,'Profesor','Salinas','Femenino','lachiquita@hotmail.com','Diseno Grafico','EDCOM'),(8,'Gonzalo','Iturburu',1001234567,987567485,'Personal Contratado','ALborada','Masculino','wachitoto@gmail.com','Ing. Alimentos','FICT'),(9,'Carlo','Lecaro',989543426,972635463,'Voluntario','Sur Portete','Masculino','muerte666@gmail.com','Ing. Electronica','FIEC'),(10,'Israel','Fernandez',1002345869,2147483647,'Profesor','Manabi','Masculino','is94@hotmail.com','Ing. Mecatronica','FIMCP');
/*!40000 ALTER TABLE `Personal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Representacion`
--

DROP TABLE IF EXISTS `Representacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Representacion` (
  `representacion_id` int(11) NOT NULL AUTO_INCREMENT,
  `representacion_parentesco` varchar(45) DEFAULT NULL,
  `representacion_representante` int(11) NOT NULL,
  `representacion_nino` int(11) NOT NULL,
  PRIMARY KEY (`representacion_id`),
  KEY `representacion_representante` (`representacion_representante`),
  KEY `representacion_nino` (`representacion_nino`),
  CONSTRAINT `fk_Representacion_1` FOREIGN KEY (`representacion_representante`) REFERENCES `Representante` (`representante_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Representacion_2` FOREIGN KEY (`representacion_nino`) REFERENCES `Nino` (`nino_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Representacion`
--

LOCK TABLES `Representacion` WRITE;
/*!40000 ALTER TABLE `Representacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `Representacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Representante`
--

DROP TABLE IF EXISTS `Representante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Representante` (
  `representante_id` int(11) NOT NULL,
  `representante_nombre` varchar(25) NOT NULL,
  `representante_apellido` varchar(25) NOT NULL,
  `representante_cedula` int(10) NOT NULL,
  `representante_telefono` int(12) NOT NULL,
  `representante_expreso` varchar(3) NOT NULL,
  PRIMARY KEY (`representante_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Representante`
--

LOCK TABLES `Representante` WRITE;
/*!40000 ALTER TABLE `Representante` DISABLE KEYS */;
INSERT INTO `Representante` VALUES (1,'ju','re',2,2,'SI'),(2,'m','n',1,1,'NO');
/*!40000 ALTER TABLE `Representante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Semillero`
--

DROP TABLE IF EXISTS `Semillero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Semillero` (
  `semillero_id` int(12) NOT NULL,
  `semillero_tipo` varchar(30) NOT NULL,
  `semillero_imagen` varchar(200) DEFAULT NULL,
  `semillero_ubicacion` varchar(45) DEFAULT NULL,
  `semillero_idPersonal` int(12) NOT NULL,
  PRIMARY KEY (`semillero_id`),
  KEY `fk_semillero_personal_idx` (`semillero_idPersonal`),
  CONSTRAINT `fk_semillero_personal` FOREIGN KEY (`semillero_idPersonal`) REFERENCES `Personal` (`personal_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Semillero`
--

LOCK TABLES `Semillero` WRITE;
/*!40000 ALTER TABLE `Semillero` DISABLE KEYS */;
/*!40000 ALTER TABLE `Semillero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Usuario` (
  `usuario_id` int(11) NOT NULL,
  `usuario_username` varchar(15) NOT NULL,
  `usuario_password` varchar(15) NOT NULL,
  PRIMARY KEY (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Venta`
--

DROP TABLE IF EXISTS `Venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Venta` (
  `venta_id` int(11) NOT NULL COMMENT 'venta_detalle, venta_fecha, venta_costo,venta_cantida,venta_IdPersonal(FK), venta_observaciones y compra con: compra_id, compra_detalle, compra_fecha, compra_gasto, compra_IdPersonal, compra_observaciones',
  `venta_detalle` varchar(50) NOT NULL,
  `venta_fecha` date NOT NULL,
  `venta_costo` decimal(10,2) NOT NULL,
  `venta_cantidad` int(11) NOT NULL,
  `venta_IdPersonal` int(11) NOT NULL,
  `venta_observaciones` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`venta_id`),
  KEY `venta_IdPersonal` (`venta_IdPersonal`),
  CONSTRAINT `fk_Venta_1` FOREIGN KEY (`venta_IdPersonal`) REFERENCES `Personal` (`personal_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Venta`
--

LOCK TABLES `Venta` WRITE;
/*!40000 ALTER TABLE `Venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `Venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'PAJA_SYSTEM'
--
/*!50003 DROP PROCEDURE IF EXISTS `contar` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `contar`(in tabla varchar(15))
begin
    declare contabla varchar(15);
    set contabla = (select lower(tabla));
    set @snt = CONCAT('select ', contabla, '_id from ', tabla, ' order by ', contabla, '_id desc limit 1;');
    PREPARE sent FROM @snt;
    EXECUTE sent;
    DEALLOCATE prepare sent;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ingresoJuego` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ingresoJuego`(in cod int, in nombre varchar(15), in imagen varchar(200),
in area varchar(15), in ubicacion varchar(50), in personal int)
BEGIN INSERT INTO Juego VALUES (cod, nombre, imagen, area, ubicacion, personal);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ingresoNino` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ingresoNino`(in cod int, in nombre varchar(25),
in apellido varchar(25), in edad int, in alergia varchar(2), in observacion varchar(45),
in semillero int)
BEGIN INSERT INTO Nino VALUES(cod, nombre, apellido, edad, alergia, observacion, semillero);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ingresoOficio` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ingresoOficio`(in cod int, in detalle varchar(45), in destinatario varchar(45),
in estado varchar(45), in tramite varchar(45), in respuesta varchar(45), in observaciones varchar(45),
in personal int)
BEGIN INSERT INTO Oficio VALUES(cod, detalle, destinatario, estado, tramite, respuesta, observaciones, personal); 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ingresoPersonal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ingresoPersonal`(in cod int, in nombre varchar(25), 
in apellido varchar(25), in cedula int, in telefono int, in tipo varchar(25), 
in direccion varchar(100), in sexo varchar(12), in correo varchar(40), in carrera varchar(30), in facultad varchar(30))
BEGIN INSERT INTO Personal VALUES(cod, nombre, apellido, cedula, telefono, tipo, direccion, sexo, correo, carrera, facultad);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ingresoRepresentacion` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ingresoRepresentacion`(in parentesco varchar(25),
in representante int, in nino int)
BEGIN INSERT INTO Representacion VALUES(parentesco, representante, nino);

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ingresoRepresentante` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ingresoRepresentante`(in cod int, in nombre varchar(25),in apellido varchar(25), 
in cedula int,in telefono int,in expreso varchar(3))
BEGIN INSERT INTO Representante VALUES(cod,nombre,apellido,cedula,telefono,expreso);

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `modificoJuego` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `modificoJuego`(in cod int, in nombre varchar(15), in imagen varchar(200),
in area varchar(15), in ubicacion varchar(50), in personal int)
BEGIN UPDATE Juego 
    set juego_nombre = nombre, juego_imagen = imagen, juego_area = area, juego_ubicacion = ubicacion, juego_IdPersonal = personal
    where juego_id=cod;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `modificoOficio` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `modificoOficio`(in cod int, in detalle varchar(45), in destinatario varchar(45),
in estado varchar(45), in tramite varchar(45), in respuesta varchar(45), in observaciones varchar(45),
in personal int)
BEGIN UPDATE Oficio 
    set oficio_detalle = detalle, oficio_destinatario = destinatario,
    oficio_estado = estado, oficio_tramite = tramite, oficio_respuesta = respuesta,
    oficio_observaciones = observaciones, oficio_IdPersonal = personal
    where oficio_id = cod;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `modificoPersonal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `modificoPersonal`(in cod int, in nombre varchar(25), 
in apellido varchar(25), in cedula int, in telefono int, in tipo varchar(25), 
in direccion varchar(100), in sexo varchar(12), in correo varchar(40), in carrera varchar(30), in facultad varchar(30))
BEGIN UPDATE Personal
	set personal_nombre = nombre, personal_apellido = apellido , personal_cedula = cedula
    , personal_telefono = telefono, personal_tipo = tipo, personal_direccion= direccion,
    personal_sexo = sexo, personal_correo = correo, personal_carrera= carrera, personal_facultad=facultad
    where personal_id = cod;  
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-02 12:28:30

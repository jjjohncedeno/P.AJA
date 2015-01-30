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
INSERT INTO `Juego` VALUES (3,'Asertijos','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/search.png','Creatividad','Oficina',6),(4,'El teto','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_Image.jpeg','Psicologia','Plazoneta',6),(5,'figuras locas','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_agregar.png','Matematicas','Cuarto 3',8),(6,'Crucigramas','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/solo_cruz.png','Distraccion','Salon interno',7),(7,'Historia ','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_agregar.png','Historia','Mesa central',5),(8,'El barco','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/search.png','Juegos','Fuera',1),(9,'Elefantito','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_agregar.png','Distraccion','Interna',8),(10,'adivinanzas','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_Image.jpeg','Lenguaje','Cuarto',1),(11,'Arbol de letras','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/search.png','Aprender','Salon',10),(12,'La macarena','/home/julio/Escritorio/BaseDatosProject/Proyecto/Imagenes/personal_Image.jpeg','Baile','Salon de baile',9);
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
  `nino_observacion` varchar(45) DEFAULT NULL,
  `nino_semillero` int(12) NOT NULL,
  PRIMARY KEY (`nino_id`,`nino_semillero`),
  KEY `fk_nino_semillero_idx` (`nino_semillero`),
  CONSTRAINT `fk_nino_semillero` FOREIGN KEY (`nino_semillero`) REFERENCES `Semillero` (`semillero_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nino`
--

LOCK TABLES `Nino` WRITE;
/*!40000 ALTER TABLE `Nino` DISABLE KEYS */;
INSERT INTO `Nino` VALUES (1,'david','',3,'No','',5);
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
  `oficio_IdPersonal` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`oficio_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Oficio`
--

LOCK TABLES `Oficio` WRITE;
/*!40000 ALTER TABLE `Oficio` DISABLE KEYS */;
INSERT INTO `Oficio` VALUES (1,'Prestamo','Ing Branny','Recibido','123','No quiero','No tengo billete','1'),(2,'Mas errores de internet','Ing. Julio','Recibido','12','No se','No he estudiado','1'),(3,'La prueba final','John','Recibido','123','No se que es','Puede que no haya ','1'),(4,'Eliminacion de materia','Rector','Recibido','1234','No se que mas','Cualquier nota','1'),(5,'nuvo ingreso','presidente','Recibido','233','pendiente','niguna','1'),(6,'ingreso de tramites ','preidencia','Recibido','2345','pendinte','ninguna','1'),(7,'proximas compras','alcaldia','Recibido','345','pendiente','niguna','1'),(8,'nuevo oficio','rectorado','Recibido','456','pendiente','niguna','1'),(9,'nuevo','rectoado','Recibido','67','nada','pendente','1'),(10,'destidno','retorado','Recibido','456','ninguna','penditne','1');
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
-- Table structure for table `Representante`
--

DROP TABLE IF EXISTS `Representante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Representante` (
  `representante_id` int(11) NOT NULL,
  `representante_nombre` varchar(25) NOT NULL,
  `representante_apellido` varchar(25) NOT NULL,
  `representante_telefono` int(12) NOT NULL,
  `representante_expreso` varchar(3) NOT NULL,
  `representante_nInscritos` int(12) NOT NULL,
  `representante_nino` int(12) NOT NULL,
  PRIMARY KEY (`representante_id`,`representante_nino`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Representante`
--

LOCK TABLES `Representante` WRITE;
/*!40000 ALTER TABLE `Representante` DISABLE KEYS */;
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
  `semillero_nIntegrantes` int(12) DEFAULT NULL,
  `semillero_imagen` varchar(100) DEFAULT NULL,
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-01-28 16:37:53

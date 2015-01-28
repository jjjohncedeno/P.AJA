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
  PRIMARY KEY (`nino_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nino`
--

LOCK TABLES `Nino` WRITE;
/*!40000 ALTER TABLE `Nino` DISABLE KEYS */;
/*!40000 ALTER TABLE `Nino` ENABLE KEYS */;
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
/*!40000 ALTER TABLE `Personal` ENABLE KEYS */;
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

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;
-- Dump completed on 2015-01-25 23:08:04


DROP TABLE IF EXISTS `Juego`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Juego` (
  `juego_id` int(11) AUTO_INCREMENT,
  `juego_nombre` varchar(15) NULL,
  `juego_imagen` varchar(15) NULL,
  `juego_area` varchar(15) NULL,
  `juego_ubicacion` varchar(15) NULL,
  `juego_IdPersonal` int(11)  NULL,
  PRIMARY KEY (`juego_id`),
  FOREIGN KEY (juego_IdPersonal) REFERENCES Personal(personal_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Juego` WRITE;
/*!40000 ALTER TABLE `Juego` DISABLE KEYS */;
/*!40000 ALTER TABLE `Juego` ENABLE KEYS */;
UNLOCK TABLES;


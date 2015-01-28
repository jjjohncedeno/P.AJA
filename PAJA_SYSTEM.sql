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
INSERT INTO `Personal` VALUES (1,'julio','realpe',49,494,'Ayudante','fjkf','Masculino','j@gmail.com','fj','jk');
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
  `semillero_nIntegrantes` int(12) NOT NULL,
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
INSERT INTO `Semillero` VALUES (1,'popo',0,'','por lo banos',1),(2,'popo',0,'','banos',1),(3,'popo',0,'','bano',1),(4,'popo',0,'','bano',1),(5,'popo',0,'','bano',1);
/*!40000 ALTER TABLE `Semillero` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-01-28 14:15:38

-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: app
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `kullanici`
--

DROP TABLE IF EXISTS `kullanici`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kullanici` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ad_soyad` text NOT NULL,
  `email` varchar(255) NOT NULL,
  `parola` text NOT NULL,
  `role` enum('Öğretim Üyesi','Öğrenci','Yönetici') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kullanici`
--

LOCK TABLES `kullanici` WRITE;
/*!40000 ALTER TABLE `kullanici` DISABLE KEYS */;
INSERT INTO `kullanici` VALUES (15,'Dr. Öğr. Üyesi Vildan YAZICI','vildan.yazici@university.edu','vildan123','Öğretim Üyesi'),(16,'Dr. Öğr. Üyesi Mehmet KARA','mehmet.kara@university.edu','mehmet123','Öğretim Üyesi'),(17,'Dr. Öğr. Üyesi Saliha ELMAS','saliha.elmas@university.edu','saliha123','Öğretim Üyesi'),(18,'Dr. Öğr. Üyesi Ulaş VURAL','ulas.vural@university.edu','ulas123','Öğretim Üyesi'),(19,'Dr. Öğr. Üyesi Fulya AKDENİZ','fulya.akdeniz@university.edu','fulya123','Öğretim Üyesi'),(20,'Dr. Öğr. Üyesi Ercan ÖLÇER','ercan.olcer@university.edu','ercan123','Öğretim Üyesi'),(21,'Dr. Öğr. Üyesi İsmet KARADUMAN','ismet.karaduman@university.edu','ismet123','Öğretim Üyesi'),(22,'Dr. Öğr. Üyesi E. Pınar HACIBEYOĞLU','pinar.hacibeyoglu@university.edu','pinar123','Öğretim Üyesi'),(23,'Prof. Dr. H. Tarık DURU','tarik.duru@university.edu','tarik123','Öğretim Üyesi'),(24,'Prof. Dr. Nevcihan DURU','nevcihan.duru@university.edu','nevcihan123','Öğretim Üyesi'),(25,'Dr. Öğr. Üyesi Ahmet Şen','ahmet.sen@university.edu','ahmet123','Öğretim Üyesi'),(26,'Öğr.Gör. DUYGU SUNMAZ ARSLAN','duygu.sunmaz@university.edu','duygu123','Öğretim Üyesi'),(27,'Yönetici','yonetici@university.edu','yonetici123','Öğretim Üyesi'),(28,'Prof. Dr. Firdevs KARAHAN','firdevs.karahan@university.edu','firdevs123','Öğretim Üyesi'),(29,'Öğrenci','ogrenci@university.edu','ogrenci123','Öğrenci'),(30,'Admin','admin@university.edu','admin123','Yönetici');
/*!40000 ALTER TABLE `kullanici` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-22 23:38:01

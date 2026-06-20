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
-- Table structure for table `dersler`
--

DROP TABLE IF EXISTS `dersler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dersler` (
  `ders_kodu` varchar(20) NOT NULL,
  `ders_adi` text NOT NULL,
  `haftalik_saat` int NOT NULL,
  `ogretim_uyesi_id` int NOT NULL,
  `bolum_kodu` varchar(10) NOT NULL,
  `derslik_id` varchar(50) NOT NULL,
  `donem` int NOT NULL,
  `akts` int NOT NULL,
  `ders_turu` enum('Zorunlu','Seçmeli') NOT NULL,
  PRIMARY KEY (`ders_kodu`),
  KEY `ogretim_uyesi_id` (`ogretim_uyesi_id`),
  KEY `bolum_kodu` (`bolum_kodu`),
  KEY `derslik_id` (`derslik_id`),
  CONSTRAINT `dersler_ibfk_1` FOREIGN KEY (`ogretim_uyesi_id`) REFERENCES `kullanici` (`id`),
  CONSTRAINT `dersler_ibfk_2` FOREIGN KEY (`bolum_kodu`) REFERENCES `bolum` (`bolum_kodu`),
  CONSTRAINT `dersler_ibfk_3` FOREIGN KEY (`derslik_id`) REFERENCES `derslik` (`derslik_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dersler`
--

LOCK TABLES `dersler` WRITE;
/*!40000 ALTER TABLE `dersler` DISABLE KEYS */;
INSERT INTO `dersler` VALUES ('ATA100','ATATÜRK İLKELERİ VE İNKILAP TARİHİ',4,28,'ORT','D401',2,4,'Zorunlu'),('BLM111','BİLGİSAYAR MÜHENDİSLİĞİNE GİRİŞ',2,24,'BLM','D102',1,3,'Zorunlu'),('BLM112','BİLGİSAYAR PROGRAMLAMA 1',3,15,'BLM','BİL.LAB.2',1,4,'Zorunlu'),('BLM113','BİLGİSAYAR LAB-I',2,18,'BLM','D102',1,3,'Zorunlu'),('BLM121','BİLGİSAYAR LAB-II',3,15,'BLM','D402',2,3,'Zorunlu'),('BLM122','BİLGİSAYAR PROGRAMLAMA II',4,18,'BLM','S202',2,4,'Zorunlu'),('BLM125','ELEKTRİK DEVRE TEMELLERİ',3,23,'BLM','D302',2,5,'Zorunlu'),('BLM211','NESNEYE YÖNELİK PROGRAMLAMA',4,18,'BLM','AMFİ B',3,5,'Zorunlu'),('BLM213','VERİ YAPILARI',4,19,'BLM','S201',4,5,'Zorunlu'),('BLM215','TEMEL ELEKTRONİK VE UYGULAMALARI',3,21,'BLM','D101',3,4,'Zorunlu'),('BLM217','PROGRAMLAMA LAB-I',3,19,'BLM','M201',3,5,'Zorunlu'),('BLM226','SAYISAL TASARIM VE UYGULAMALARI',4,21,'BLM','D101',4,4,'Zorunlu'),('BLM230','VERİTABANI YÖNETİM SİSTEMLERİ',4,19,'BLM','D301',3,5,'Zorunlu'),('BLM232','PROGRAMLAMA LAB-II',2,24,'BLM','S101',4,3,'Zorunlu'),('BLM311','İŞLETİM SİSTEMLERİ',3,21,'BLM','D401',6,5,'Zorunlu'),('BLM313','YAZILIM MÜHENDİSLİĞİ',4,20,'BLM','D104',5,5,'Zorunlu'),('BLM315','YAZILIM LAB-I',2,22,'BLM','KÜÇÜK LAB',5,4,'Zorunlu'),('BLM317','BİLGİSAYAR AĞLARI',4,16,'BLM','KÜÇÜK LAB',4,5,'Zorunlu'),('BLM320','ALGORİTMA TASARIMI VE ANALİZİ',3,22,'BLM','D402',6,5,'Zorunlu'),('BLM321','YAPAY ZEKA',3,21,'BLM','D102',5,5,'Zorunlu'),('BLM328','BİLGİSAYAR MİMARİSİ VE ORGANİZASYONU',3,22,'BLM','S101',5,4,'Zorunlu'),('BLM334','YAZILIM LAB-II',2,22,'BLM','AMFİ B',6,5,'Zorunlu'),('BLM411','PROGRAMLAMA DİLLERİ',3,19,'BLM','D301',7,5,'Seçmeli'),('BLM413','BİÇİMSEL DİLLER VE OTOMATLAR',3,19,'BLM','S201',7,5,'Zorunlu'),('BLM415','ARAŞTIRMA PROBLEMLERİ',2,15,'BLM','S201',7,2,'Zorunlu'),('BLM417','İŞ SAĞLIĞI VE GÜVENLİĞİ-I',2,25,'BLM','D202',7,2,'Zorunlu'),('BLM420','BİLİŞİM ETİĞİ VE HUKUKU',3,24,'BLM','D401',8,4,'Zorunlu'),('BLM426','İŞ SAĞLIĞI VE GÜVENLİĞİ-II',2,25,'BLM','KÜÇÜK LAB',8,2,'Zorunlu'),('DİL100','İNGİLİZCE',4,26,'ORT','KÜÇÜK LAB',1,4,'Zorunlu'),('FIZ110','FİZİK I',5,17,'ORT','D101',1,5,'Zorunlu'),('FIZ120','FİZİK II',5,17,'ORT','D301',2,5,'Zorunlu'),('MAT110','MATEMATİK I',5,15,'ORT','D202',1,5,'Zorunlu'),('MAT120','MATEMATİK II',5,15,'ORT','M301',2,5,'Zorunlu'),('MAT125','LİNEER CEBİR',3,23,'ORT','D301',1,3,'Zorunlu'),('MAT211','DİFERANSİYEL DENKLEMLER',3,15,'BLM','BİL.LAB.2',3,4,'Zorunlu'),('MAT213','AYRIK MATEMATİK',4,15,'ORT','AMFİ A',3,4,'Zorunlu'),('MAT220','SAYISAL YÖNTEMLER',3,15,'ORT','BİL.LAB.2',5,4,'Zorunlu'),('MAT224','OLASILIK VE İSTATİSTİK',3,15,'ORT','AMFİ A',4,4,'Zorunlu'),('S018','ALAN SEÇMELİ DERS I',3,27,'ORT','D201',5,4,'Zorunlu'),('S019','ALAN SEÇMELİ DERS II',3,27,'ORT','BİL.LAB 1',6,4,'Seçmeli'),('S020','ALAN SEÇMELİ DERS III',3,27,'ORT','D102',7,4,'Zorunlu'),('S021','ALAN SEÇMELİ DERS IV',3,27,'ORT','D104',7,4,'Zorunlu'),('S022','ALAN SEÇMELİ DERS V',3,27,'ORT','AMFİ B',8,4,'Seçmeli'),('S023','ALAN SEÇMELİ DERS VI',3,27,'ORT','D401',8,4,'Seçmeli'),('TUR100','TÜRK DİLİ',4,28,'ORT','D202',2,4,'Zorunlu'),('US001','ÜNİVERSİTE SEÇMELİ DERS I',2,27,'ORT','KÜÇÜK LAB',1,3,'Seçmeli'),('US002-BLM','ÜNİVERSİTE SEÇMELİ DERS II',2,27,'BLM','KÜÇÜK LAB',3,3,'Seçmeli'),('US002-YZM','ÜNİVERSİTE SEÇMELİ DERS II',2,27,'YZM','AMFİ A',3,3,'Zorunlu'),('US003-BLM','ÜNİVERSİTE SEÇMELİ DERS III',2,27,'BLM','BİL.LAB.2',4,3,'Seçmeli'),('US003-YZM','ÜNİVERSİTE SEÇMELİ DERS III',2,27,'YZM','D401',3,3,'Seçmeli'),('US004-BLM','ÜNİVERSİTE SEÇMELİ DERS IV',2,27,'BLM','M201',5,3,'Zorunlu'),('US004-YZM','ÜNİVERSİTE SEÇMELİ DERS IV',2,27,'YZM','S201',4,3,'Seçmeli'),('US005-BLM','ÜNİVERSİTE SEÇMELİ DERS V',2,27,'BLM','D103',6,3,'Seçmeli'),('US005-YZM','ÜNİVERSİTE SEÇMELİ DERS V',2,27,'YZM','BİL.LAB 1',5,3,'Seçmeli'),('US006-BLM','ÜNİVERSİTE SEÇMELİ DERS VI',2,27,'BLM','KÜÇÜK LAB',6,3,'Seçmeli'),('US006-YZM','ÜNİVERSİTE SEÇMELİ DERS VI',2,27,'YZM','S201',6,3,'Seçmeli'),('US007-BLM','ÜNİVERSİTE SEÇMELİ DERS VII',2,27,'BLM','S202',7,3,'Seçmeli'),('US008-BLM','ÜNİVERSİTE SEÇMELİ DERS VIII',2,27,'BLM','D101',7,3,'Zorunlu'),('US009-BLM','ÜNİVERSİTE SEÇMELİ DERS IX',2,27,'BLM','D101',8,3,'Seçmeli'),('US010-BLM','ÜNİVERSİTE SEÇMELİ DERS X',2,27,'BLM','M101',8,3,'Seçmeli'),('YZM113','BİLGİSAYAR PROGRAMLAMA-I',3,15,'YZM','S202',1,4,'Zorunlu'),('YZM115','BİLGİSAYAR LAB-I',2,18,'YZM','KÜÇÜK LAB',1,3,'Zorunlu'),('YZM117','BİLGİSAYAR LAB-II',3,15,'YZM','BİL.LAB 1',2,3,'Zorunlu'),('YZM119','YAZILIM MÜHENDİSLİĞİNE GİRİŞ',2,24,'YZM','KÜÇÜK LAB',1,3,'Zorunlu'),('YZM122','BİLGİSAYAR PROGRAMLAMA II',4,18,'YZM','D403',2,4,'Zorunlu'),('YZM127','PROGRAMLAMA LAB-I',3,19,'YZM','D301',3,5,'Zorunlu'),('YZM128','WEB TEKNOLOJİLERİ',3,16,'YZM','S201',2,5,'Zorunlu'),('YZM213','VERİ YAPILARI',4,19,'YZM','AMFİ A',4,5,'Zorunlu'),('YZM219','YAZILIM GEREKSİNİM ANALİZİ',3,22,'YZM','D202',3,5,'Zorunlu'),('YZM224','VERİTABANI YÖNETİM SİSTEMLERİ',4,19,'YZM','D403',3,5,'Zorunlu'),('YZM226','YAZILIM TASARIMI',4,20,'YZM','D104',4,4,'Zorunlu'),('YZM228','PROGRAMLAMA LAB-II',2,24,'YZM','S202',4,3,'Zorunlu'),('YZM229','NESNEYE YÖNELİK PROGRAMLAMA',4,18,'YZM','D202',3,5,'Zorunlu'),('YZM312','İŞLETİM SİSTEMLERİ',3,21,'YZM','M301',6,5,'Zorunlu'),('YZM317','BİLGİSAYAR AĞLARI',4,16,'YZM','S202',4,5,'Zorunlu'),('YZM319','WEB PROGRAMLAMA',3,19,'YZM','AMFİ A',5,4,'Zorunlu'),('YZM326','BİLGİSAYAR MİMARİSİ VE ORGANİZASYONU',3,22,'YZM','AMFİ A',5,4,'Zorunlu'),('YZM329','YAZILIM TEST VE KALİTE',3,22,'YZM','D101',5,3,'Zorunlu'),('YZM330','YAZILIM LAB- II',2,22,'YZM','D104',6,4,'Zorunlu'),('YZM331','YAZILIM LAB-I',2,22,'YZM','M301',5,4,'Zorunlu'),('YZM332','ALGORİTMA TASARIMI VE ANALİZİ',3,22,'YZM','AMFİ A',6,4,'Zorunlu'),('YZM335','YAPAY ZEKA',3,21,'YZM','S202',5,4,'Zorunlu'),('YZM411','YAZILIM PROJE YÖNETİMİ',4,20,'YZM','M101',6,5,'Zorunlu');
/*!40000 ALTER TABLE `dersler` ENABLE KEYS */;
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

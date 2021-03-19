CREATE DATABASE  IF NOT EXISTS `cecl` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `cecl`;
-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: cecl
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `task` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `union_train` tinyint(4) NOT NULL,
  `edge_nodes` varchar(255) DEFAULT NULL,
  `file` text,
  `status` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (1,'测试任务','2020-05-31 11:15:54',NULL,NULL,0,'nodes','file',0),(2,'测试任务1','2020-05-31 12:08:33','2020-05-31 12:11:49','2020-05-31 12:29:45',0,'nodes','train.py',3),(3,'mnist','2020-05-31 12:09:21',NULL,NULL,0,'nodes','train.py',0),(4,'测试二','2020-05-31 12:10:20',NULL,NULL,0,'nodes','train.py',0),(5,'test_task','2020-05-31 12:11:07',NULL,NULL,0,'nodes','train.py',0),(6,'测试任务','2020-07-24 17:47:48',NULL,NULL,0,'','todo.txt',0),(7,'测试任务1','2020-07-24 17:49:29',NULL,NULL,0,'','todo.txt',0),(8,'mnist','2020-07-24 17:49:50',NULL,NULL,0,'','todo.txt',0),(9,'测试二','2020-07-24 17:51:58',NULL,NULL,0,'','todo.txt',0),(10,'test_task','2020-07-24 17:53:35',NULL,NULL,0,'','todo.txt',0),(11,'测试任务','2020-07-24 17:53:53',NULL,NULL,0,'','todo.txt',0),(12,'测试任务1','2020-07-24 17:54:30',NULL,NULL,0,'','todo.txt',0),(13,'mnist','2020-07-24 22:44:28',NULL,NULL,0,'','test.py',0),(14,'测试二','2020-07-24 22:49:38',NULL,NULL,0,'','test.py',0),(15,'test_task','2020-07-24 22:50:49',NULL,NULL,0,'','test.py',0),(17,'测试任务','2020-07-24 23:16:30',NULL,NULL,0,'','test.py',0),(18,'test','2020-07-24 23:24:38',NULL,NULL,0,'','test.py',0),(19,'测试文件','2020-07-24 23:27:02',NULL,NULL,0,'','test.py',0),(22,'test1456','2020-07-24 23:32:16',NULL,NULL,0,'','test.py',0),(23,'test453','2020-07-24 23:33:35',NULL,NULL,0,'','test.py',0),(24,'test45323af','2020-07-24 23:36:05',NULL,NULL,0,'','test.py',0),(25,'test45323af','2020-07-24 23:38:26',NULL,NULL,0,'','test.py',0),(26,'test45323af','2020-07-24 23:38:39',NULL,NULL,0,'','test.py',0),(27,'test45323af1','2020-07-24 23:42:11',NULL,NULL,0,'','test.py',0),(28,'test45323af2','2020-07-24 23:43:35',NULL,NULL,0,'','test.py',0),(29,'test45323af3','2020-07-24 23:44:04',NULL,NULL,0,'','test.py',0),(30,'test45323af4','2020-07-24 23:45:36',NULL,NULL,0,'','test.py',0),(31,'test45323af5','2020-07-24 23:46:31',NULL,NULL,0,'','test.py',0),(32,'testa1','2020-07-24 23:47:44',NULL,NULL,0,'','test.py',0),(33,'testa2','2020-07-24 23:48:12',NULL,NULL,0,'','test.py',0),(34,'testa3','2020-07-24 23:53:24',NULL,NULL,0,'','test.py',0),(35,'testa5','2020-07-24 23:54:51',NULL,NULL,0,'','test.py',0),(36,'testa6','2020-07-24 23:56:03',NULL,NULL,0,'','test.py',0),(37,'testa7','2020-07-24 23:58:59',NULL,NULL,0,'','test.py',0),(38,'testa8','2020-07-25 00:03:06',NULL,NULL,0,'','test.py',0),(39,'testa9','2020-07-25 00:03:50',NULL,NULL,0,'','test.py',0),(40,'testa10','2020-07-25 00:04:15',NULL,NULL,0,'','test.py',0),(41,'testa11','2020-07-25 00:06:35',NULL,NULL,0,'','test.py',0),(42,'testa12','2020-07-25 00:10:34',NULL,NULL,0,'','test.py',0),(43,'testa13','2020-07-25 00:10:56',NULL,NULL,0,'','test.py',0),(44,'testa14','2020-07-25 00:13:17',NULL,NULL,0,'','test.py',0),(45,'testa15','2020-07-25 00:14:15','2020-07-25 00:14:14',NULL,0,'','test.py',1),(46,'testa16','2020-07-25 00:15:09','2020-07-25 00:15:09',NULL,0,'','test.py',1),(47,'testa18','2020-07-25 00:16:20','2020-07-25 00:16:20',NULL,0,'','test.py',1),(48,'testa20','2020-07-25 00:27:31','2020-07-25 00:27:30','2020-07-25 00:27:30',0,'','test.py',1),(49,'testa21','2020-07-25 00:29:12','2020-07-25 00:29:12','2020-07-25 00:29:12',0,'','test.py',1),(50,'testa23','2020-07-25 00:31:17','2020-07-25 00:31:17','2020-07-25 00:31:17',0,'','test.py',1),(51,'testa25','2020-07-25 00:34:41','2020-07-25 00:34:40','2020-07-25 00:34:40',0,'','test.py',1),(52,'testa26','2020-07-25 00:35:48','2020-07-25 00:35:48','2020-07-25 00:35:48',0,'','test.py',1),(53,'testaaa','2020-07-25 18:13:26','2020-07-25 18:13:26','2020-07-25 18:13:26',0,'','test.py',1),(54,'test阿尔法','2020-07-25 18:15:17','2020-07-25 18:15:17','2020-07-25 18:15:17',0,'','test.py',1),(55,'test阿尔法f ','2020-07-25 18:15:49','2020-07-25 18:15:48','2020-07-25 18:15:48',0,'','test.py',1),(56,'测试','2020-07-25 19:33:46','2020-07-25 19:33:46','2020-07-25 19:33:45',0,'','test.py',1),(57,'测试','2020-07-25 19:34:31','2020-07-25 19:34:31','2020-07-25 19:34:31',0,'','test.py',1),(58,'测试','2020-07-25 19:37:17','2020-07-25 19:37:27','2020-07-25 19:37:27',1,'','test.py',1),(59,'测试','2020-07-25 19:37:22','2020-07-25 19:37:31','2020-07-25 20:49:51',1,'','test.py',3),(60,'test','2020-07-25 19:49:46',NULL,'2020-07-25 20:39:11',0,'','test.py',3);
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_log`
--

DROP TABLE IF EXISTS `task_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `task_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_log_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_log`
--

LOCK TABLES `task_log` WRITE;
/*!40000 ALTER TABLE `task_log` DISABLE KEYS */;
INSERT INTO `task_log` VALUES (1,1,'Test!!','2020-06-02 23:09:43'),(2,1,'Test!!','2020-06-02 23:23:55'),(3,1,'Test!!','2020-06-03 23:28:36'),(4,1,'Test!!','2020-06-03 23:31:25'),(5,1,'Test!!','2020-06-03 23:35:04'),(6,1,'Test!!','2020-06-03 23:35:58'),(7,1,'开始训练 0','2020-06-04 00:33:49'),(8,1,'开始训练 0\r\n开始训练 1\r\n开始训练 2\r\n开始训练 3\r\n开始训练 4\r\n测试训练错误的情况 0\r\n测试训练错误的情况 1\r\n测试训练错误的情况 2\r\n测试训练错误的情况 3\r\n测试训练错误的情况 4\r\n','2020-06-04 00:37:18'),(9,1,'开始训练 0\r\n开始训练 1\r\n开始训练 2\r\n开始训练 3\r\n开始训练 4\r\n测试训练错误的情况 0\r\n测试训练错误的情况 1\r\n测试训练错误的情况 2\r\n测试训练错误的情况 3\r\n测试训练错误的情况 4\r\n','2020-06-07 19:11:08'),(10,1,'开始训练 0\r\n开始训练 1\r\n开始训练 2\r\n开始训练 3\r\n开始训练 4\r\n测试训练错误的情况 0\r\n测试训练错误的情况 1\r\n测试训练错误的情况 2\r\n测试训练错误的情况 3\r\n测试训练错误的情况 4\r\n','2020-06-07 19:15:35'),(11,1,'Using TensorFlow backend.\r\nWARNING: Logging before flag parsing goes to stderr.\r\nW0607 20:19:45.442040 13624 deprecation_wrapper.py:119] From C:\\Program Files\\Python36\\lib\\site-packages\\keras\\backend\\tensorflow_backend.py:4070: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.\r\n\r\nModel: \"sequential_1\"\r\n_________________________________________________________________\r\nLayer (type)                 Output Shape              Param #   \r\n=================================================================\r\nconv2d_1 (Conv2D)            (None, 26, 26, 32)        320       \r\n_________________________________________________________________\r\nactivation_1 (Activation)    (None, 26, 26, 32)        0         \r\n_________________________________________________________________\r\nconv2d_2 (Conv2D)            (None, 24, 24, 32)        9248      \r\n_________________________________________________________________\r\nactivation_2 (Activation)    (None, 24, 24, 32)        0         \r\n_________________________________________________________________\r\nmax_pooling2d_1 (MaxPooling2 (None, 12, 12, 32)        0         \r\n_________________________________________________________________\r\nconv2d_3 (Conv2D)            (None, 10, 10, 64)        18496     \r\n_________________________________________________________________\r\nactivation_3 (Activation)    (None, 10, 10, 64)        0         \r\n_________________________________________________________________\r\nconv2d_4 (Conv2D)            (None, 8, 8, 64)          36928     \r\n_________________________________________________________________\r\nactivation_4 (Activation)    (None, 8, 8, 64)          0         \r\n_________________________________________________________________\r\nmax_pooling2d_2 (MaxPooling2 (None, 4, 4, 64)          0         \r\n_________________________________________________________________\r\nflatten_1 (Flatten)          (None, 1024)              0         \r\n_________________________________________________________________\r\ndense_1 (Dense)              (None, 512)               524800    \r\n_________________________________________________________________\r\nactivation_5 (Activation)    (None, 512)               0         \r\n_________________________________________________________________\r\ndropout_1 (Dropout)          (None, 512)               0         \r\n_________________________________________________________________\r\ndense_2 (Dense)              (None, 10)                5130      \r\n_________________________________________________________________\r\nactivation_6 (Activation)    (None, 10)                0         \r\n=================================================================\r\nTotal params: 594,922\r\nTrainable params: 594,922\r\nNon-trainable params: 0\r\n_________________________________________________________________\r\nTraceback (most recent call last):\r\n  File \"./uploads/1/train.py\", line 58, in <module>\r\n    height_shift_range=0.08, zoom_range=0.08)\r\n  File \"C:\\Program Files\\Python36\\lib\\site-packages\\keras\\preprocessing\\image.py\", line 292, in __init__\r\n    dtype=dtype)\r\nTypeError: __init__() got an unexpected keyword argument \'interpolation_order\'\r\n','2020-06-07 20:19:45'),(12,31,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-24 23:46:30'),(13,32,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-24 23:47:43'),(14,33,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-24 23:48:11'),(15,34,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-24 23:53:23'),(16,35,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-24 23:54:51'),(17,36,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-24 23:56:03'),(18,37,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-24 23:58:59'),(19,38,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:03:06'),(20,39,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:03:49'),(21,40,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:04:15'),(22,42,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:10:33'),(23,43,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:10:55'),(24,44,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:13:16'),(25,45,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:14:14'),(26,46,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:15:09'),(27,47,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:16:20'),(28,48,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:27:30'),(29,48,'<_InactiveRpcError of RPC that terminated with:\n	status = StatusCode.UNKNOWN\n	details = \"Exception calling application: \'FinishTaskResp\' object has no attribute \'code\'\"\n	debug_error_string = \"{\"created\":\"@1595608050.640000000\",\"description\":\"Error received from peer ipv4:127.0.0.1:50053\",\"file\":\"src/core/lib/surface/call.cc\",\"file_line\":1056,\"grpc_message\":\"Exception calling application: \'FinishTaskResp\' object has no attribute \'code\'\",\"grpc_status\":2}\"\n>','2020-07-25 00:27:30'),(30,49,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:29:12'),(31,49,'<_InactiveRpcError of RPC that terminated with:\n	status = StatusCode.UNKNOWN\n	details = \"Exception calling application: \'FinishTaskResp\' object has no attribute \'code\'\"\n	debug_error_string = \"{\"created\":\"@1595608152.246000000\",\"description\":\"Error received from peer ipv4:127.0.0.1:50053\",\"file\":\"src/core/lib/surface/call.cc\",\"file_line\":1056,\"grpc_message\":\"Exception calling application: \'FinishTaskResp\' object has no attribute \'code\'\",\"grpc_status\":2}\"\n>','2020-07-25 00:29:12'),(32,50,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:31:17'),(33,51,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:34:40'),(34,52,'[1, 2, \'e\', 3, 4, 5]\r\n','2020-07-25 00:35:48'),(35,53,'0\r\n1\r\n2\r\n3\r\n4\r\n0\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n11\r\n12\r\n13\r\n14\r\n15\r\n16\r\n17\r\n18\r\n19\r\n','2020-07-25 18:13:26'),(36,54,'0\r\n1\r\n2\r\n3\r\n4\r\n0\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n11\r\n12\r\n13\r\n14\r\n15\r\n16\r\n17\r\n18\r\n19\r\n','2020-07-25 18:15:16'),(37,55,'0\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n11\r\n12\r\n13\r\n14\r\n0\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n11\r\n12\r\n13\r\n14\r\n15\r\n16\r\n17\r\n18\r\n19\r\n20\r\n21\r\n22\r\n23\r\n24\r\n25\r\n26\r\n27\r\n28\r\n29\r\n30\r\n31\r\n32\r\n33\r\n34\r\n35\r\n36\r\n37\r\n38\r\n39\r\n40\r\n41\r\n42\r\n43\r\n44\r\n45\r\n46\r\n47\r\n48\r\n49\r\n50\r\n51\r\n52\r\n53\r\n54\r\n55\r\n56\r\n57\r\n58\r\n59\r\n60\r\n61\r\n62\r\n63\r\n64\r\n65\r\n66\r\n67\r\n68\r\n69\r\n70\r\n71\r\n72\r\n73\r\n74\r\n75\r\n76\r\n77\r\n78\r\n79\r\n80\r\n81\r\n82\r\n83\r\n84\r\n85\r\n86\r\n87\r\n88\r\n89\r\n90\r\n91\r\n92\r\n93\r\n94\r\n95\r\n96\r\n97\r\n98\r\n99\r\n','2020-07-25 18:15:48'),(38,56,'0\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n11\r\n12\r\n13\r\n14\r\n0\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n7\r\n8\r\n9\r\n10\r\n11\r\n12\r\n13\r\n14\r\n15\r\n16\r\n17\r\n18\r\n19\r\n20\r\n21\r\n22\r\n23\r\n24\r\n25\r\n26\r\n27\r\n28\r\n29\r\n30\r\n31\r\n32\r\n33\r\n34\r\n35\r\n36\r\n37\r\n38\r\n39\r\n40\r\n41\r\n42\r\n43\r\n44\r\n45\r\n46\r\n47\r\n48\r\n49\r\n50\r\n51\r\n52\r\n53\r\n54\r\n55\r\n56\r\n57\r\n58\r\n59\r\n60\r\n61\r\n62\r\n63\r\n64\r\n65\r\n66\r\n67\r\n68\r\n69\r\n70\r\n71\r\n72\r\n73\r\n74\r\n75\r\n76\r\n77\r\n78\r\n79\r\n80\r\n81\r\n82\r\n83\r\n84\r\n85\r\n86\r\n87\r\n88\r\n89\r\n90\r\n91\r\n92\r\n93\r\n94\r\n95\r\n96\r\n97\r\n98\r\n99\r\n','2020-07-25 19:33:45'),(39,57,'test\r\n','2020-07-25 19:34:31'),(40,58,'finish\r\n','2020-07-25 19:37:27'),(41,59,'finish\r\n','2020-07-25 19:37:31'),(42,60,'finish\r\n','2020-07-25 19:49:56');
/*!40000 ALTER TABLE `task_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-27 11:14:09

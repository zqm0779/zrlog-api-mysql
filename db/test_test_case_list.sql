-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `test_case_list`
--

DROP TABLE IF EXISTS `test_case_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_case_list` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '测试用例编号',
  `web` varchar(255) DEFAULT NULL COMMENT '项目名称',
  `module` varchar(255) DEFAULT NULL COMMENT '项目模块',
  `title` varchar(255) DEFAULT NULL COMMENT '测试用例的标题',
  `url` varchar(255) DEFAULT NULL COMMENT '接口地址的路径',
  `method` varchar(255) DEFAULT NULL COMMENT '请求方法',
  `headers` varchar(255) DEFAULT NULL COMMENT '请求头',
  `cookies` varchar(1000) DEFAULT NULL COMMENT 'cookies密钥',
  `request_body` varchar(2000) DEFAULT NULL COMMENT '请求主体信息',
  `request_type` varchar(255) DEFAULT NULL COMMENT '请求主体的数据类型',
  `relation` varchar(255) DEFAULT NULL COMMENT '关联',
  `expected_code` varchar(255) DEFAULT NULL COMMENT '预期业务状态码',
  `isdel` int DEFAULT '1' COMMENT '测试用例是否可运行（0为删除，1为正常）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3 COMMENT='测试用例表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_case_list`
--

LOCK TABLES `test_case_list` WRITE;
/*!40000 ALTER TABLE `test_case_list` DISABLE KEYS */;
INSERT INTO `test_case_list` VALUES (1,'zrlog','登录模块','密码错误','/api/admin/login','post','{\"Content-Type\": \"application/json\"}','{}','{\"userName\":\"admin\",\"password\":123456,\"https\":False}','json','','9010',1),(2,'zrlog','登录模块','不携带密码参数','/api/admin/login','post','{\"Content-Type\": \"application/json\"}','{}','{\"userName\":\"admin\",\"https\":False}','json','','9009',1),(3,'zrlog','登录模块','用户名错误','/api/admin/login','post','{\"Content-Type\": \"application/json\"}','{}','{\"userName\":\"adminx\",\"password\":\"2f7110622dc770f8dce166c93e13ce03\",\"https\":False}','json','','9010',1),(4,'zrlog','登录模块','用户名为非字符串类型','/api/admin/login','post','{\"Content-Type\": \"application/json\"}','{}','{\"userName\":123456,\"password\":\"2f7110622dc770f8dce166c93e13ce03\",\"https\":False}','json','','9010',1),(5,'zrlog','登录模块','不携带用户名参数','/api/admin/login','post','{\"Content-Type\": \"application/json\"}','{}','{\"password\":\"2f7110622dc770f8dce166c93e13ce03\",\"https\":False}','json','','9009',1),(6,'zrlog','登录模块','用户名为空字符串','/api/admin/login','post','{\"Content-Type\": \"application/json\"}','{}','{\"userName\":\"\",\"password\":\"2f7110622dc770f8dce166c93e13ce03\",\"https\":False}','json','','9009',1),(7,'zrlog','登录模块','用户名和密码正确','/api/admin/login','post','{\"Content-Type\": \"application/json\"}','{}','{\"userName\":\"root\",\"password\":\"b2e14b919db67e50a19cc0f507f5f370\",\"https\":False}','json','token=cookies.admin-token','0',1),(8,'zrlog','文章管理模块','发布文章','/api/admin/article/create','post','{\"Content-Type\": \"application/json\"}','{\"admin-token\":\"${token}\"}','{\"id\":None,\"editorType\":\"markdown\",\"title\":\"付出\",\"alias\":\"付出\",\"thumbnail\":None,\"typeId\":\"1\",\"keywords\":None,\"digest\":None,\"canComment\":False,\"recommended\":False,\"privacy\":False,\"content\":\"<p>付出</p>\\n\",\"markdown\":\"付出\",\"rubbish\":False}','json','id_name=body.id,alias_name=body.alias','0',1),(9,'zrlog','文章管理模块','修改文章','/api/admin/article/update','post','{\"Content-Type\": \"application/json\"}','{\"admin-token\":\"${token}\"}','{\"id\":\"${id_name}\",\"editorType\":\"markdown\",\"title\":\"付出才能杰出\",\"alias\":\"${alias_name}\",\"thumbnail\":None,\"typeId\":\"1\",\"keywords\":None,\"digest\":\"<p>付出</p>\",\"canComment\":False,\"recommended\":False,\"privacy\":False,\"content\":\"<p>付出</p>\\n\",\"markdown\":\"付出\",\"rubbish\":False}','json','','0',1),(10,'zrlog','文章管理模块','删除文章','/api/admin/article/delete','post','{\"Content-Type\": \"application/x-www-form-urlencoded\"}','{\"admin-token\":\"${token}\"}','{\"oper\":\"del\",\"id\":\"${id_name}\"}','data','','0',1),(11,'zrlog','文章管理模块','查询文章','/api/admin/article?keywords=付出才能杰出&_search=false&nd=1598429806679&rows=10&page=1&sidx=&sord=asc','get','{\"Content-Type\": \"application/x-www-form-urlencoded\"}','{\"admin-token\":\"${token}\"}','{}','data','','0',1);
/*!40000 ALTER TABLE `test_case_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-16 22:31:29

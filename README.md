# ZrLog_Autotest
基于pytest+request的接口自动化开源框架

----
#### 模块类的设计
`requestsutil.py` 封装request方法，可以支持多协议扩展（get\post）

`config.py` 配置文件，包括：目录的配置，数据库连接配置

`logutil.py` 封装记录log方法

`base.py` 封装核心的方法

`log` 存放日志

`report` 存放报告

`mysqlutil.py` mysql数据库操作工具类

`readmysql.py` 读取mysql数据库测试数据

`test_run.py` 定义并执行用例集

`pytest.ini` 测试框架的配置文件，制定运行规则

----
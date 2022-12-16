# coding=utf-8
import os
# 获取文件的绝对路径
abs_path = os.path.abspath(__file__)
# print(abs_path)
# 获取文件所在目录的上一级目录,也就是根目录
project_path = os.path.dirname(os.path.dirname(abs_path))
# 通过os.sep的方法来获取config目录的全路径
#os.sep获取系统的分隔符，windows系统常用分隔符为\或\\,而linux分隔符为/,避免不同系统平台出现拼接不兼容导致问题
_conf_path = project_path + os.sep + "configure"
# 通过os.sep的方法来获取log日志目录的全路径
_log_path = project_path + os.sep + "log"
# 通过os.sep的方法来获取report报告目录的全路径
_report_path = project_path + os.sep + "report"

# 数据库信息配置
DB_CONFIG = {"host": "127.0.0.1",
             "user": "root",
             "password": "gmcc1234!@#$",
             "database": "test",
             "port": 3306,
             "charset": "utf8"}


# 返回日志目录
def get_log_path():
    return _log_path


# 返回报告目录
def get_report_path():
    return _report_path


# 返回config目录
def get_config_path():
    return _conf_path


# 占位用，勿删除
class DynamicParam:
    pass


# 测试代码
if __name__ == '__main__':
    print(get_log_path())
    print(get_report_path())
    print(get_config_path())

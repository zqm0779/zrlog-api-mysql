# coding=utf-8
# 导入PyMySQL库
import traceback

import pymysql
# 导入数据库的配置信息
from configure.config import DB_CONFIG
# 导入记录日志的对象
from tools.logutil import logger


# 设置数据库工具类的名称
class MysqlUtil:
    def __init__(self):
        # 读取配置文件，初始化pymysql数据库连接
        self.db = pymysql.connect(**DB_CONFIG)
        # 创建数据库游标
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    # 获取单条数据
    def get_fetchone(self, sql):
        # 执行sql
        self.cursor.execute(sql)
        # 查询单条数据，结果返回
        return self.cursor.fetchone()

    # 获取多条数据
    def get_fetchall(self, sql):
        # 执行sql
        self.cursor.execute(sql)
        # 查询多条数据，结果返回
        return self.cursor.fetchall()

    # 执行更新类sql
    def sql_execute(self, sql):
        # noinspection PyBroadException
        try:
            # db对象和指针对象同时存在
            if self.db and self.cursor:
                # 执行sql
                self.cursor.execute(sql)
                # 提交执行sql到数据库，完成insert或者update相关命令操作，非查询时使用
                self.db.commit()
        except Exception as e:
            # 出现异常时，数据库回滚
            self.db.rollback()
            # 打印日志
            logger.error("sql语句执行错误，已执行回滚操作")
            traceback.print_exc(e)
            # 返回结果为失败
            return False

    # 关闭对象，staticmethod静态方法，可以直接使用类名.静态方法。
    @staticmethod
    def close(self):
        # 判断游标对象是否存在
        if self.cursor is not None:
            # 存在则关闭指针
            self.cursor.close()
        # 判断数据库对象是否存在
        if self.db is not None:
            # 存在则关闭数据库对象
            self.db.close()


# 测试代码
if __name__ == '__main__':
    mysql = MysqlUtil()
    res = mysql.get_fetchall("select * from test_case_list")
    print(res)
    MysqlUtil.close(mysql)

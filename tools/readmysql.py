# coding=utf-8
# 导入datetime库
import datetime
# 导入json库
import json
# 导入MysqlUtil类
from tools.mysqlutil import MysqlUtil
# 导入logger对象
from tools.logutil import logger
# 初始化mysql工具类
mysql = MysqlUtil()


# 定义获取测试用例类
class RdTestcase:
    # 加载所有的测试用例
    def load_all_case(self, web):
        # 定义sql语句，根据条件web查询test_case表中所有测试用例
        sql = f"select * from `test_case_list` where web = '{web}'"
        # 调用工具类方法，获取所有数据
        results = mysql.get_fetchall(sql)
        # 返回结果
        return results

    # 筛选可执行的用例
    def is_run_data(self, web):
        # 根据条件isdel==1筛选可执行的测试用例列表
        run_list = [case for case in self.load_all_case(web) if case['isdel'] == 1]
        # 返回可执行测试用例列表
        return run_list

    # 获取配置信息
    def load_confkey(self, web, key):
        # 根据web和key,查询test_config相关配置信息
        sql = f"select * from `test_config` where web='{web}' and `key`='{key}'"
        # 调用方法查询1条结果
        results = mysql.get_fetchone(sql)
        # 返回结果
        return results

    # 更新测试结果
    def update_results(self, response, is_pass, case_id):
        # 获取当前时间
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 更新测试用例执行结果，插入test_result表
        sql = f"insert into `test_result_record`(case_id,times,response,result) values ('{case_id}','{current_time}','{json.dumps(response, ensure_ascii=False)}','{is_pass}')"
        # 执行insert操作
        rows = mysql.sql_execute(sql)
        # 打印日志
        logger.debug(sql)
        # 返回更新结果True/False
        return rows


# 测试代码
if __name__ == '__main__':
    test = RdTestcase()
    print(test.is_run_data('zrlog'))
    print(test.load_confkey('zrlog', 'test'))
    # res = test.update_results({'code': 200, 'body': {'error': 1, 'message': '用户名和密码都不能为空'}, 'cookies': {}}, 'True', '1')
    # print(res)

# coding=utf-8
from configure.config import get_log_path
import logging
import time
import os
# 设置变量，目的为了控制日志信息是否在控制台输出，True为输出，False为不输出
STREAM = True


class LogUtil:
    def __init__(self):
        # 初始化日志对象，设置日志名称
        self.logger = logging.getLogger("logger")
        # 设置总的日志级别开关
        self.logger.setLevel(logging.DEBUG)
        # 避免日志重复
        if not self.logger.handlers:
            # 定义日志名称
            self.log_name = '{}.log'.format(time.strftime("%Y_%m_%d", time.localtime()))
            # 定义日志路径及文件名称
            self.log_path_file = os.path.join(get_log_path(), self.log_name)
            # 定义文件处理handler
            fh = logging.FileHandler(self.log_path_file, encoding='utf-8', mode='a')
            # 设置文件处理handler的日志级别
            fh.setLevel(logging.DEBUG)
            # 日志格式变量
            formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            # 设置打印格式
            fh.setFormatter(formatter)
            # 添加handler
            self.logger.addHandler(fh)
            # 关闭handler
            fh.close()
            # 控制台输出
            if STREAM:
                # 定义控制台输出流handler
                fh_stream = logging.StreamHandler()
                # 控制台输出日志级别
                fh_stream.setLevel(logging.DEBUG)
                # 设置打印格式
                fh_stream.setFormatter(formatter)
                # 添加handler
                self.logger.addHandler(fh_stream)

    def log(self):
        # 返回定义好的logger对象，对外直接使用log函数即可
        return self.logger


logger = LogUtil().log()
# 测试代码
if __name__ == '__main__':
    logger.info('test')

import logging

"""
format 格式参数
%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID
%(message)s：打印日志信息
"""

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s -%(threadName)s - %(filename)s[:%(lineno)d] - %(name)s - %(levelname)s - %(message)s')
    logging.debug("this is a debug")
    logging.info("this is a info")
    logging.warning("this is a warning")
    logging.error("this is a error")

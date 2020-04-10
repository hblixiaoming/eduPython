import logging
import logging.handlers

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

FMT_STR = '%(asctime)s - %(threadName)s - %(filename)s[:%(lineno)d] - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger("myLogger")
logger.setLevel(logging.DEBUG)

fileHandler = logging.handlers.TimedRotatingFileHandler(filename='all.log', when='midnight', interval=1)
fileFormatter = logging.Formatter(fmt=FMT_STR)
fileHandler.setFormatter(fileFormatter)

consoleHandler = logging.StreamHandler()
consoleFormatter = logging.Formatter(fmt=FMT_STR)
consoleHandler.setFormatter(consoleFormatter)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

if __name__ == '__main__':
    logger.debug("this is debug")
    logger.info("this is info")
    logger.warning("this is warning")
    logger.error("this is error")

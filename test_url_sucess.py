#!/usr/bin/python
# coding=utf8
"""
python2
install urllib3
"""
import Queue
import logging
import threading
import time
import re
import requests
queue = Queue.Queue()

class Mythread(threading.Thread):
    def __init__(self, queue):
        super(Mythread, self).__init__()
        self.queue = queue

    def run(self):
        # while not queue.empty():
        while True:
            url = self.queue.get()
            print url
            url0 = re.findall('(.*)\..*IN',url)[0]
            url1='http://'+url0
            url2 = 'https://'+url0
            try:
                rep = requests.get(url1,timeout=20)
                true_url.append(url)
            except Exception as e:
                try:
                    rep1 = requests.get(url2,timeout=20)
                    true_url.append(url)
                except Exception as e:
                    false_url.append(url)

            self.queue.task_done()


def main():
    with open("A_record.txt","r") as url_req:
        for x in url_req:
            x=x.strip()
            queue.put(x)
    for i in range(20):
        t = Mythread(queue)  # 调用线程的工作函数
        t.setDaemon(True)
        t.start()
        time.sleep(0.1)
    # 当队列中的 url 被执行完成，接触阻塞
    queue.join()  # 主线程在此等待 queue这个子线程 完成再解除阻塞，往下执行


if __name__ == '__main__':
    # 创建日志记录器
    logger_name = "example"
    logger = logging.getLogger(logger_name)  # 创建实例
    logger.setLevel(logging.DEBUG)  # 设置 日志记录的级别
    # 创建日志处理器
    log_path = "./log.log"
    fh = logging.FileHandler(log_path)  # 创建 文件处理器，并输出到日志文件
    fh.setLevel(logging.WARN)  # 设置 日志处理器的 处理级别
    # 创建 日志显示格式
    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)  # 创建 格式对象
    #  把创建好的格式赋给处理器
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    true_url = []
    false_url = []
    main()
    with open('true.txt','a+') as tr_url:
        for tr in true_url:
            tr = tr + " 2"
            tr_url.write(tr)
            tr_url.write('\n')
    with open('fa_url.txt','a+') as fa_url:
        for fa in false_url:
            fa = fa + " 1"
            fa_url.write(fa)
            fa_url.write('\n')
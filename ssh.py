#!/usr/bin/python
# coding=utf8
"""
python2
install urllib3
"""
import Queue
import ftplib
import logging
import sys
import threading
import time
import paramiko

queue = Queue.Queue()


class Mythread(threading.Thread):
    def __init__(self, queue):
        super(Mythread, self).__init__()
        self.queue = queue

    def run(self):
        # while not queue.empty():
        while True:
            pwd = self.queue.get()
            for username in username_list:
                user = username.rstrip()
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(ip,port, user, pwd, timeout=20)
                    print('[+] FTP weak password: ' + user, pwd)
                except:
                    print('[-] checking for ' + user, pwd + ' fail')
            self.queue.task_done()


def main():
    for passwd in password_list:
        pwd = passwd.rstrip()
        queue.put(pwd)
    for i in range(5):
        t = Mythread(queue)  # 调用线程的工作函数
        t.setDaemon(True)
        t.start()
        time.sleep(0.3)
    # 当队列中的 url 被执行完成，接触阻塞
    queue.join()  # 主线程在此等待 queue这个子线程 完成再解除阻塞，往下执行


if __name__ == '__main__':
    ip = sys.argv[1]
    port = 22
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
    username_list = ['root','admin']
    password_list = ['root', 'toor','admin','p@ssw0rd','p@$$w0rd','p@ssw0rd>?','p@$$w0rd>?','!@#123qwe','123qwe!@#']
    main()

from multiprocessing  import Process
import os
from redis import StrictRedis
from time import sleep

#初始化redis连接
r = StrictRedis(host='192.168.1.36', port=7002, db=1)

#在终端运行队列中的命令
def start_train(cmd):
    os.system(cmd)

#循环检测redis队列
while 1:
    while r.llen('queue') != 0:
        #获取队列头元素
        cmd = (r.rpop('queue'))
        #print(cmd)
        p = Process(target=start_train, args=(cmd,))
        p.start()
        print('开始训练')
        sleep(5)




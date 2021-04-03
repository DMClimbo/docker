from multiprocessing  import Process
import os
from redis import StrictRedis



r = StrictRedis(host='192.168.1.36', port=7002, db=1)

def start_train(cmd):
    os.system(cmd)


while 1:
    while r.llen('queue') != 0:
        cmd = (r.rpop('queue'))
        print(cmd)
        print('开始训练')
        p = Process(target=start_train, args=(cmd,))
        p.start()




from multiprocessing  import Process
import os 

flask_run = 'python ./background.py'
request_queue_run = 'python ./request_queue.py'


def start_process(cmd):
    os.system(cmd)


#启动后台和检测队列进程
if __name__ == "__main__":
    p1 = Process(target=start_process, args=(flask_run,))
    p1.start()
    print('flask后端启动成功')
    p2 = Process(target=start_process, args=(request_queue_run,))
    p2.start()
    print('请求队列启动成功')
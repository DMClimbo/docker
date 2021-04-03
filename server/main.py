from multiprocessing  import Process
import os 

Start_server = 'python ./webserver.py'
Start_check_queue = 'python ./check_queue.py'


def start_process(cmd):
    os.system(cmd)


#启动后台和检测队列进程
if __name__ == "__main__":
    #启动flask后端
    Server = Process(target=start_process, args=(Start_server,))
    Server.start()
    print('web后端启动成功')

    #启动检测队列程序
    Check_queue = Process(target=start_process, args=(Start_check_queue,))
    Check_queue.start()
    print('请求队列启动成功')
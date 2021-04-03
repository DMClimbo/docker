from flask import Flask,request, jsonify
import subprocess
import os 
import yaml, json

from functions import handle_json 
from flask_cors import CORS
from redis import StrictRedis

#连接redis数据库
r = StrictRedis(host='192.168.1.36', port=7002, db=1)

#解决跨域问题
app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/', methods=['POST','GET'])
def get_json():
    #接收到post请求后新建文件夹保存训练结果
    if  request.method =='POST':

        json_get = request.get_data(as_text=True)
        json_dict = json.loads(json_get)
        
        #创建文件夹并生成yaml配置文件返回训练命令
        cmd = handle_json(json_dict)
        print(cmd)
        #将命令插入队列
        try:
            r.lpush('queue', cmd)
        except Exception as e:
            print(e)

    return "请求已插入队列"

    if  request.method == 'GET':
        return "服务器正常，可以发送训练请求"




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)




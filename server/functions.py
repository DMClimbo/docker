
from multiprocessing import Process
import os 
import yaml, json
import requests
import pymysql
import zipfile

def handle_json(json_dict):
    #创建文件夹保存训练参数和结果
        outputdir = r'/cv/output/' +  json_dict["USER"] + '_' + json_dict["MODEL_NAME"]
        os.mkdir(outputdir)
        
        # 修改保存模型位置和数据集文件夹为绝对路径
        json_dict["MODEL"]["MODEL_SAVE_DIR"] = outputdir
        dataset_dir = get_dataset(json_dict)
        json_dict["DATASET"]["IMAGE_ROOT"] = dataset_dir

        #生成yaml配置文件
        yaml_file = open(outputdir + '/config.yaml','w')
        yaml.safe_dump(json_dict, stream=yaml_file, default_flow_style=False)

        print("生成配置文件")
        return "python /cv/project/train.py --config " + outputdir + "/config.yaml"
        # return True


#检查数据集是否存在，若不存在则下载并创建
def get_dataset(json_dict):
    dataset_dir = '/cv/data/' + json_dict['DATASET']['TRAINSET'] + '_' + json_dict['DATASET']['VERSION'] + '/'
    if(os.path.exists(dataset_dir)):
        print('数据集已存在')
    else:
        os.mkdir(dataset_dir)
        url = json_dict['URL']
        file_path = dataset_dir + json_dict['DATASET']['VERSION'] + '.zip'
        get_file(url, file_path)
        unzip(dataset_dir)
        # download_images(url,dataset_dir)
    return dataset_dir


#下载文件
def get_file(url, file_path):  
    try:
        r = requests.get(url, stream=True)  ##修改
        content = requests.get(url).content  # 这里必须用.content而不能用text
        print('开始下载')
        with open(file_path, "wb") as f:
            f.write(content)

        if r.status_code == 200:
            return r.content
        elif r.status_code == 404:
            print ("File not found" )
            return None
    except Exception as e:
        print("Could not get file. Exception is: %s" % e)

    return "download successed"


#解压zip文件并合并
def unzip(storage_path):
    file_list = os.listdir(storage_path)
    for file_name in file_list:
        if os.path.splitext(file_name)[1] == '.zip':
            file_name = storage_path + file_name
            file_zip = zipfile.ZipFile(file_name, 'r')
            for file in file_zip.namelist():
                file_zip.extract(file, storage_path)
            file_zip.close()
            os.remove(file_name)



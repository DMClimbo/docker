生成镜像：docker build -t  REPOSITORY:TAG  .

生成容器：sudo docker run -itd --runtime=nvidia  --shm-size="8g" --name  classfication -p9001:9000 -v /etc/localtime:/etc/localtime:ro REPOSITORY:TAG  /bin/bash

修改容器属性：1.docker ps -a 查看容器ID
            2.su以root用户进入目录: cd /var/lib/docker/containers/容器ID
            3.修改hostconfig.json文件

复制文件进容器：关闭容器后运行 docker cp 目标文件  容器ID:期望容器内位置

将容器打包成镜像：docker commit  容器ID   REPOSITORY:TAG


docker修改容器默认存储路径(不修改的话默认占用系统盘空间)：
    （1）创建docker容器存放的路径
        # mkdir -p /home/data/docker/lib

    （2）停止Docker服务并迁移数据到新目录
        # systemctl stop docker.service
        # rsync -avz /var/lib/docker/ /home/data/docker/lib/

    （3）创建Docker配置文件
        # mkdir -p /etc/systemd/system/docker.service.d/ 
        # vim /etc/systemd/system/docker.service.d/devicemapper.conf
        [Service]
        ExecStart=
        ExecStart=/usr/bin/dockerd  --graph=/home/data/docker/lib/

     (4）重启Docker服务
        # systemctl daemon-reload 
        # systemctl restart docker
    
    （5）查看现在容器存放的目录
        # docker info | grep "Dir"
        Docker Root Dir: /home/data/docker/lib
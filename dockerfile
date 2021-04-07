
#版本：cuda10.0 ubuntu18.04
FROM nvidia/cuda:10.0-devel-ubuntu18.04
 
ENV LANG C.UTF-8
 
#创建目录cv并设为工作目录
COPY . /cv/
WORKDIR /cv/
 
#设置国内镜像源  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse" >/etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse" >>/etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse" >>/etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse" >>/etc/apt/sources.list
 
 
#安装软件和配置
RUN apt update && apt install -y vim && apt install -y python3.6 && apt install -y python3-pip && apt install -y curl
RUN ln -s /usr/bin/python3 /usr/bin/python && ln -s /usr/bin/pip3  /usr/bin/pip   
RUN mkdir ~/.pip && touch ~/.pip/pip.conf && 、
    echo "[global]" >~/.pip/pip.conf && \
    echo "index-url = http://mirrors.aliyun.com/pypi/simple" >>~/.pip/pip.conf && \
    echo "[install]" >>~/.pip/pip.conf && \
    echo "trusted-host=mirrors.aliyun.com" >>~/.pip/pip.conf
#RUN apt-get install libbsd0 libice6 libsm6 multiarch-support x11-common
#RUN apt-get install libxrender1
#RUN apt-get install libxext-dev

#安装训练所需库
RUN python -m pip install --upgrade pip && pip install -r ./project/requirements.txt


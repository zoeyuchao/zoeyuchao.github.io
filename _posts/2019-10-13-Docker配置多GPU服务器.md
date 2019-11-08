---
layout: post
title: Docker配置多GPU服务器
date: 2019-10-13
author: zoe
tags: tools
---

# Docker配置多GPU服务器

## 1.宿主配置

1. 安装显卡驱动
2. 安装docker

```Shell
 sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 

 sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 

 sudo apt-get update 

 sudo apt-get install -y docker-ce 
```

3. 测试是否安装成功
```Shell 
 sudo docker run hello-world
```

4. 安装nvidia-docker2

```Shell
# Add the package repositories
curl -s -L https:*//nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

curl -s -L https:*//nvidia.github.io/nvidia-docker/ubuntu16.04/amd64/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update
# install
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd

#重启docker
sudo systemctl daemon-reload
sudo systemctl restart docker
```
5. 备注docker的常用命令

```Shell
#开启docker
systemctl start docker
#关闭docker
systemctl stop docker
#列出本地已有镜像
docker images
#删除容器
docker rm xxxx
#启动容器，如果已经存在了，可以这么用，否则要先create，或者用run
docker start xxx
#重启容器
docker restart xxxx
#查看所有容器
docker ps -a
#重命名容器
docker rename oldname newname
```

6. 配置组
```Shell
$sudo groupadd docker	#添加docker用户组
$sudo gpasswd -a $USER docker	#将登陆用户加入到docker用户组中
$newgrp docker	#更新用户组
```

## 2.配置开始

1. pull一个基础镜像

   ```Shell
   sudo docker pull nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04
   ```

2. 如果是docker run

   1. 启动这个镜像

   ```Shell
   docker run --runtime=nvidia -dit --privileged --name=demo -h=thudrone nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04 /bin/bash
   ```

   -d：后台守护进程启动（否则退出就是关闭）

   -t：进入终端

   -i：获得交互式链接，获取container的输入

   --name：容器名字

   -h：主机名字

   -p：端口转发，用于远程ssh

   /bin/bash:启动一个bash shell

   这个时候container运行在后台，如果想进入它的终端，则：

   ```Shell
   docker attach goofy_almeida
   ```

   就可以了。

   使用“docker attach”命令进入container（容器）有一个缺点，那就是每次从container中退出到前台时，container也跟着退出了。

   要想退出container时，让container仍然在后台运行着，可以使用“docker exec -it”命令。每次使用这个命令进入container，当退出container后，container仍然在后台运行，命令使用方法如下：

   ```bash
   docker exec -it goofy_almeida /bin/bash
   ```

   这样输入“exit”或者按键“Ctrl + C”退出container时，这个container仍然在后台运行，通过：

3. 如果是nvidia-docker

    ```Shell
    nvidia-docker run -dit --privileged --name=demo -h=thudrone nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04 /bin/bash
    ```

## 3.一个完全空的ubuntu配置

```Shell
apt-get update
apt-get install net-tools -y
apt-get install inetutils-ping
```

```Shell
apt-get install vim
cp /etc/apt/sources.list /etc/apt/sources.list.bak
rm /etc/apt/sources.list
vim /etc/apt/sources.list 
# 添加清华源 https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/
apt-get update
apt-get install openssh-server
cd /etc/ssh
```

修改sshd_config配置文件，把  #PermitRootLogin prohibit-password 改为  `PermitRootLogin yes`

```Shell
# 设置root密码
passwd root
#开启
service ssh start
cd /home
vim startup.sh
```

```
#!/bin/bash
service ssh start
/bin/bash
```

```Shell
chmod 777 startup.sh
```

然后把cuda搞一下，写到环境变量中去。

需要的话安装一下桌面

```Shell
apt-get install ubuntu-desktop
```

写好了之后变成一个docker images

```Shell
docker commit oldname newname
```

然后从这个images重新启动一个容器

```Shell
nvidia-docker run -dit -p 2502:22 --privileged --user=demo --shm-size=2G -e DISPLAY=:10.0 --name=test -h=thudrone ubuntu-ros-ssh /bin/bash
```

之后就可以远程登录了，ip是主机ip，-p写一个2502，会遇到X11 forwarding request failed on channel 0的错误，解决方案是

```Shell
 vim /etc/ssh/sshd_config 
```

 写上一句 X11UseLocalhost no ，然后重启一下ssh服务即可。

```Shell
/etc/init.d/ssh restart  
```

## 4.开启所有容器

```
nvidia-docker start $(docker ps -a | awk '{ print $1}' | tail -n +2)
```


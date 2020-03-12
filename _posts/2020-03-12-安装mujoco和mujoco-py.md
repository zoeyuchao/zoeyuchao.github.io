---
layout: post
title: 安装mujoco和mujoco-my
date: 2020-03-12
author: zoe
tags: tools
---

# 安装mujoco和mujoco-my

## 1.简介

   官方网站： [https://www.roboti.us/index.html]( https://www.roboti.us/index.html ) 

   MuJoCo（Multi-Joint dynamics with Contact）是一个物理模拟器，可以用于机器人控制优化等研究。  

## 2.安装mujoco

1. 在[官网上](https://www.roboti.us/)下载自己需要的文件，同时点击`Licence`下载许可证，需要`full name` `email address` `computer id` 等信息，其中根据使用平台下载 `getid_linux（可执行文件）` 获取 `computer id`。 

   ```Shell
chmod a+x getid_linux (给予执行权限)
./getid_linux
   ```
   点击`submit` 后，从输入的邮箱中下载证书`mjkey.txt`。

2. 环境配置
   2.1 创建隐藏文件夹并将 `mjpro150_linux` 拷贝到 `.mujoco` 文件夹中

```shell
mkdir ~/.mujoco
cp mujoco200_linux.zip ~/.mujoco
cd ~/.mujoco
unzip mujoco200_linux.zip
mv mujoco200_linux mujoco200
```

​	2.2 将证书`mjkey.txt`拷贝到创建的隐藏文件夹中

```shell
cp mjkey.txt ~/.mujoco 
```

​	2.3.添加环境变量，打开`~/.zshrc` 文件,将以下命令添加进去

```shell
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:/home/yuchao/.mujoco/mujoco200/bin:$LD_LIBRARY_PATH"
```

​	如果不是默认的路径，可以增加:

```shell
export MUJOCO_PY_MJKEY_PATH=/home/xxx/.mujoco/mjkey.txt
export MUJOCO_PY_MUJOCO_PATH=/home/xxx/.mujoco/mojuco200
```

## 3.安装mujoco-my

官网： https://github.com/openai/mujoco-py 

```
pip install -U 'mujoco-py<2.1,>=2.0'
```

-i: 指定库的安装源

-U:升级 原来已经安装的包，不带U不会装新版本，带上U才会更新到最新版本。

可以简单测试一下：

   ```shell
   >>> import mujoco_py
   >>> from os.path import dirname
   >>> model = mujoco_py.load_model_from_path(dirname(dirname(mujoco_py.__file__))  +"/xmls/claw.xml")
   >>> sim = mujoco_py.MjSim(model)
   >>> print(sim.data.qpos)
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
   >>> sim.step()
   >>> print(sim.data.qpos)
   [ 2.09217903e-06 -1.82329050e-12 -1.16711384e-07 -4.69613872e-11
    -1.43931860e-05  4.73350204e-10 -3.23749942e-05 -1.19854057e-13
    -2.39251380e-08 -4.46750545e-07  1.78771599e-09 -1.04232280e-08]
   ```

   


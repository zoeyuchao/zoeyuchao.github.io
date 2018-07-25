---
layout: post
title: OPENWRT + USB摄像头 网页显示
date: 2018-07-25
author: 阿金
cover: https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3590010943,200237664&fm=27&gp=0.jpg
tags: 嵌入式 技术
---

> 该项目主要完成在嘉兴爱迪曼（天控科技）的开发板配置。

## 项目总体描述

在该项目中，要求摄像头通过USB接入 MT7288 开发板。用户端的电脑通过 LAN 或者 与 开发板的 WLAN or WIFI 在同一局域网中。用户端电脑通过 IP 地址在 CHROME 浏览器中实时获取 USB 摄像头的图像。

利用端口映射，可以很轻易将开发板的某个网络端口映射到公网服务器上，从而让客户端通过公网服务器获取实时图像。关于端口映射，可以参考之前的文章。

http://yujincheng.me/2018/07/17/OpewrtMT7628.html#关于自动映射

整个实验过程可分为如下三部。

1. 安装摄像头驱动

2. 配置mjpg-streamer

3. 浏览器访问。

### 安装摄像头驱动

需要在编译固件的时候，在 ```make menuconfig```阶段选择如下几个选项。

```Shell
<*> kmod-video-core #安装摄像头驱动
    <*>   kmod-video-uvc
    -*-   kmod-video-videobuf2

    <*> kmod-usb-ohci
    <*> kmod-usb-uhci

<*> mjpg-streamer #安装软件
```

编译后重新烧写固件。

如果固件编译成功，插上USB摄像头之后会在 ```/dev/``` 目录下生成一个video节点。

```Shell
    root@OpenWrt:/\# ls /dev/video0
    /dev/video0
```

## 配置启动mjpg-streamer

### 启动mjpg-streamer

在板子上面执行下面两条命令其中的一条,对于 YUV 格式的摄像头：

```Shell
    mjpg_streamer -i "input_uvc.so -f 10 -r 320*240 -y" -o "output_http.so -w www"
```

对于支持mjpeg格式的摄像头：

```Shell
    mjpg_streamer -i "input_uvc.so -f 10 -r 320*240" -o "output_http.so -w www"
```

可以得到如下输出，说明摄像头的流已经被成功推送到路由器的 8080 端口。

```Shell
[root@openwrt mjpg-streamer]\# ./mjpg_streamer
MJPG Streamer Version.: 2.0
 i: Using V4L2 device.: /dev/video0
 i: Desired Resolution: 640 x 480
 i: Frames Per Second.: 5
 i: Format............: MJPEG
 o: www-folder-path...: disabled
 o: HTTP TCP port.....: 8080
 o: username:password.: disabled
 o: commands..........: enabled
```

### mjpg-streamer 参数简要说明

-i 表示指定输入，这里输入为：input_uvc.so即uvc(usb video)。
-d 是设备 位置，我们摄像头的设备位置在：/dev/video0。
-y 用于区分一般摄像头和支持MJPEG的 摄像头。
-o指定输出，这里输出到 output_ http.so即http(可以理解为输出到网页上)。
-w 指定web服务器为www。

-y 是关键，默认启动是 mjpeg 格式，这个就报错。改成 YUV 格式
-d 指定设备
-f 制定帧数，默认 30 帧
-r 指定视频大小，如 320×240
-q 指定画质，默认 80 关于输出参数：
-p 指定端口，这里是 8080
-w 指定网页目录，这里我们设置的是/www/camwww 目录
-c 设置通过密码访问

## 通过浏览器访问

只有比较高级的浏览器，比如火狐、CHROME可以直接访问。IE和EDGE都不好使。

先确定路由器板子的地址：假如为 10.10.1.1

则在客户端浏览器的地址栏输入：

```Shell
    http://10.10.1.1:8080/?action=stream
```

即可显示摄像头实时影像。

## 参考资料

1. [github地址](https://github.com/jacksonliam/mjpg-streamer)

1. [博客1](https://blog.csdn.net/aa120515692/article/details/47803839)

2. [博客2](https://blog.csdn.net/zhaole20094463/article/details/7026252)

3. [官网](https://openwrt.org/docs/guide-user/hardware/video/webcam?s[]=mjpg&s[]=stream)

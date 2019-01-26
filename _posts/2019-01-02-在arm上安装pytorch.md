---
layout: post
title: PyTorch在ARM上的安装
date: 2019-01-02
author: JC Yu
tags: tools
---

# PyTorch在ARM上的安装

## 环境：  
ZCU102，Ubuntu16.04 LTS  

## 1.安装流程：  
pytorch可以用conda、编译版本和pip安装x86版，但是好像都不支持ARM架构，所以使用源码安装
* 1.1 下载源码  
输入  
&emsp;```git clone --recursive https://github.com/pytorch/pytorch```  

* 1.2 安装  
在文件夹下有setup.py文件，输入  
&emsp;```python setup.py install```  
等待完成即可

## 2.可能遇到的问题   

* 2.1  
	Could not find /home/linaro/pytorch/torch/lib/gloo/CMakeLists.txt  
输入  
```git submodule update --init --recursive```  

* 2.2  git clone 过慢  
解决办法：  
在 https://www.ipaddress.com/  
这个网址上查找  github.global.ssl.fastly.net github.com的ip  
输入  
&emsp;```$ sudo vim /etc/host```
将上述网址和ip加进去，输入  
&emsp;```sudo /etc/init.d/networking restart```  
即可 

* 2.3  Can't find module named "torch_C"  
重启系统即可
---
layout: post
title: TincVPN + OpenWRT 配置
date: 2018-07-20
author: 阿金
cover: https://www.tinc-vpn.org/images/tinclogo.png
tags: 嵌入式
---

> 该项目主要完成在嘉兴爱迪曼（天控科技）的开发板配置。 4G网络通过映射到局域网中，实现局域网内的视频录像机于田间地头的网络摄像头连接。

# 任务目标

项目构成图如下所示，
![poster](/post_img/2018-07-20/struct.png "struct")

硬盘录像机接在路由器a上，摄像头接在路由器b上，路由器a在控制室里，路由器b为上篇文章中配置的4G网络路由器，利用4G网路接入，分布在田间地头。

海康威视提供了硬盘录像机，在硬盘录像机中配置摄像头的IP地址即可对摄像头进行录像、打开、关闭、等操作。

本次试验主要配置路由器a，路由器b，以及公网VPS，三个节点，在此三个节点中利用tinc配置VPS，建立局域网，之后通过配置网络转发和防火墙，实现网络摄像机对于网络摄像头b1、b2的控制。

其中，路由器a、路由器b，均部署openwrt系统，公网VPS为ubuntu系统。

# TINC 安装

在 openwrt 上，使用包管理软件对程序进行安装。在本次应用过程中，我们采用源码编译的模式进行安装，通过配置 ```make menuconfig -> network -> VPN -> tinc 实现```。

```shell
opkg update
opkg install tinc
```

在 ubuntu上，也可以使用包管理程序进行安装。

```shell
sudo apt-get update
sudo apt-get install tinc
```

# VPS 中配置

在 ubuntu 上对tinc进行配置。

TINC要求同一个VPN各个节点的网络名称一致。假设我们的VPN网络名称为 vpnTK。

每一个节点需要一个名字，在本实验中，公网VPS的节点名称为bwh1，路由器a名称为213j，路由器b的节点名称为214j。

## tinc文件组成

首先，需要讲一下 tinc在 ubuntu 上文件组成。

```Shell
/etc/tinc/nets.boot             #（1）指定需要启动的VPN名称
        /vpnTK/rsa_key.priv     # 私钥匙，这个文件是后面使用命令自动产生的，不是手工编辑出来的
              /tinc.conf        #（2）主要的配置文件
              /tinc-up          #（3）启动VPN时执行的脚本，一般配置IP地址
              /tinc-down        #（4）关闭VPN时执行的脚本，一般关闭网卡
              /hosts/bwh1       # (5) 配置文件夹，VPN中各个节点该文件夹存放的内容应该一致
                    /213j
                    /214j
```

## tinc配置

在 tinc 启动时，/usr/sbin/tincd 程序会首先读取nets.boot 确定要启动的名称。

### nets.boot

在 nets.boot 中填入VPN名称： vpnTK。/etc/tinc/net.boot 如下：

```Shell
##This file contains all names of the networks to be started on system startup.
vpnTK
```

### tinc.conf

之后 编辑 /etc/tinc/vpnTK/tinc.conf，如下

```Shell
Name=bwh1         #节点名称
Port=18655        #默认为655，我们在这里修改
Interface=tun0    #设置虚拟网卡的名称
```

### tinc-up/tinc-donw

接着编辑 /etc/tinc/vpnTK/tinc-up, 主要是设置虚拟网卡的ip地址，如下

```Shell
ifconfig $INTERFACE 172.18.1.1 netmask 255.255.255.0
```

接着编辑 /etc/tinc/vpnTK/tinc-down, 目标是关闭网卡，如下

```Shell
ifconfig $INTERFACE down
```

### 生成秘钥

然后就是生成 私钥文件 /etc/tinc/vpnTK/rsa_key.priv，和对应的公钥 /etc/tinc/vpnTK/hosts/bwh1

首先编辑 公钥的头部，打开/新建 /etc/tinc/vpnTK/hosts/bwh1 文件。写入实际的IP地址（域名）和子网地址域。

```Shell
Address=yujc.eva7.nics.cc 18655 #域名空格后接端口号，我们之前配置的就是 18655
Subnet=172.18.1.1/32
```

编辑完成公钥头部之后，就可以生成对应的公钥和私钥了。在shell中执行命令。按照提示（默认选择路径）生成对应的公钥私钥。其中私钥路径为 /etc/tinc/vpnTK/rsa_key.priv。 公钥会写在/etc/tinc/vpnTK/hosts/bwh1 头部之后。

```Shell
tincd -n vpnTK -K4096
```

至此，VPS上的ubuntu配置已经完成。

# OpenWRT 中配置

与ubuntu上类似，openwrt的tinc配置具备类似的文件组成结构。区别在于没有tinc.conf文件，该文件被映射为 /etc/config/tinc。目录结构如下:

```Shell
/etc/config/tinc                #（2）主要的配置文件
/etc/tinc/nets.boot             #（1）指定需要启动的VPN名称
        /vpnTK/rsa_key.priv     # 私钥匙，这个文件是后面使用命令自动产生的，不是手工编辑出来的
              /tinc-up          #（3）启动VPN时执行的脚本，一般配置IP地址
              /tinc-down        #（4）关闭VPN时执行的脚本，一般关闭网卡
              /hosts/bwh1       # (5) 配置文件夹，VPN中各个节点该文件夹存放的内容应该一致
                    /213j
                    /214j
```

## tinc配置

主要是配置文件 /etc/config/tinc 文件，其中比较关键的选项如下（以路由器a为例，只需要修改相应地址即可配置路由器b）：

```Shell
config tinc-net vpnTK
        list ConnectTo bwh1
        #option Name 214j
        option Name 213j
        option Interface vpnTK
        option PrivateKeyFile /etc/tinc/tinc/rsa_key.priv

#config tinc-host 214j
config tinc-host 213j
        option enabled 1
        option net vpnTK
        option Port 18655
        #option Subnet 10.10.2.0/24
        option Subnet 10.10.1.0/24  # 该配置表示子网（LAN）的流量允许通过该节点
```

### tinc-up/tinc-down

接着编辑 /etc/tinc/vpnTK/tinc-up、tinc-down，脚本需要添加执行权限，脚本中以ip开头的命令使用需要安装ip-full，若没有安装使用命令opkg install ip-full。

tinc-up（以路由器a的配置为例）:

```Shell
#!/bin/sh
ip='172.18.1.3'                                 # 214 虚拟网卡的ip地址
ip link set $INTERFACE up                       # 打开虚拟网卡
ip addr add $ip/24 dev $INTERFACE               # 设置虚拟网卡地址
ip route add 10.10.2.0/24 dev $INTERFACE        # 设置流量转发，所有要访问 10.10.2/24 的流量都从 新建的虚拟网卡发出
```

tinc-down，关闭虚拟网卡，添加的IP地址以及路由条目会自动消失:

```Shell
ifconfig $INTERFACE down
```

## 生成秘钥

再之后，还是配置 公钥私钥。

先配置公钥头，打开/新建 /etc/tinc/vpnTK/hosts/213j 文件。写入实际的IP地址（域名）和子网地址域。

```Shell
Subnet=172.18.1.3/32
Subnet=10.10.1.0/24
```

注意，这里已经配置了两个Subnet，一个为路由器lan口的Subnet，10.10.1.0/24，另一个是vps的Subnet，172.18.1.3。

之后和类似ubuntu配置类似，先添加 /etc/tinc/vpnTK/tinc.conf，只需要NAME属性即可

```Shell
Name=213j         #节点名称
```

编辑完成公钥头部之后,和配置文件之后，就可以生成对应的公钥和私钥了。在shell中执行命令。按照提示（默认选择路径）生成对应的公钥私钥。其中私钥路径为 /etc/tinc/vpnTK/rsa_key.priv。 公钥会写在/etc/tinc/vpnTK/hosts/213j 头部之后。

```Shell
tincd -n vpnTK -K4096
```

至此，openwrt上的tinc配置完成。

# 交换秘钥

先下载三个文件：

1. 公网VPS中的 /etc/tinc/vpnTK/hosts/bwh1 文件

2. 路由器a 中的 /etc/tinc/vpnTK/hosts/213j 文件

3. 路由器b 中的 /etc/tinc/vpnTK/hosts/214j 文件

之后将这三个文件都拷贝到 三个设备的 /etc/tinc/vpnTK/hosts 目录中。

# 准备启动

在启动之前，再次检查，三个设备的 /etc/tinc/vpnTK/tinc-up (tinc-down) 文件是否具备可执行权限。

之后，开始配置网卡和IP地址。

## ubuntu 网卡配置 和 启动

确认是否具备 /dev/net/tun 文件，如果不具备，请新建该模块，在终端中执行：

```Shell
sudo mkdir -p /dev/net
sudo mknod /dev/net/tun c 10 200
```

之后可以启动tinc，来提供服务了。终端中执行启动调试模式（可以通过 Ctrl+\ 来终止）：

```Shell
tincd -n hello -D --debug=3
```

## openwrt 网卡和防火墙配置

### 虚拟网卡添加

在/etc/config/network 中添加一个虚拟网卡，

```Shell
config interface 'tinc'
    option ifname 'tun0'
    option defaultroute '0'
    option peerdns '0'
    option proto 'none'
```

### 修改LAN地址

并且修改 openwrt 中lan口的地址，在/etc/config/network找到类似代码段并且修改如下，以路由器a为例。

```Shell
config interface 'lan'
        option ifname 'eth0.1'
        option force_link '1'
        option macaddr '0c:ef:af:cf:e1:b2'
        option type 'bridge'
        option proto 'static'
        option ipaddr '10.10.1.1'   # 主要就是修改这一行，确定IP地址，路由器a地址为这个。路由器b地址为 10.10.2.1
        option netmask '255.255.255.0'
        option ip6assign '60'
```

### 配置防火墙

在 /etc/config/network 中添加防火墙区域，并设定转发规则。

```Shell
config zone
        option input 'ACCEPT'
        option output 'ACCEPT'
        option name 'tinc'
        option forward 'ACCEPT'
        option network 'tinc'

config forwarding
        option dest 'lan'
        option src 'tinc'

config forwarding
        option dest 'tinc'
        option src 'lan'
```

## openwrt 启动tinc

重启网络

```Shell
/ect/init.d/network restart
```

重启防火墙

```Shell
/ect/init.d/firewall restart
```

重启tinc

```Shell
/ect/init.d/tinc restart
```

至此，tinc配置全部完成。网络摄像机可以直接ping通 10.10.1.3。

# 参考资料

1. [http://blog.kompaz.win/2017/03/30/OpenWRT%20tinc/](http://blog.kompaz.win/2017/03/30/OpenWRT%20tinc/)

2. [http://www.lucktu.com/archives/763.html](http://www.lucktu.com/archives/763.html)
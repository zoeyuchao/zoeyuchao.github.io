---
layout: post
title: Debian系统无法DHCP上网
date: 2019-01-18
author: 阿金
tags: 调试笔记
---

# Debian系统无法DHCP上网

## 错误描述

使用深鉴科技的ZU9配合深鉴科技的BOOT.bin文件，文件配置中采用静态IP上网，这显然是不够让人满意的。

我们想修改为 DHCP 上网。

我们直接修改 /etc/network/interfaces 关于eth0的配置如下。

```Text
auto eth0
iface eth0 inet dhcp
```

重启之后，发现并不能拿到IP。

这是因为深鉴科技的文件系统没有安装 dhcp的客户端，导致服务dhcp上网。

## 解决方案

首先，采用静态的IP的形式连上网线再说。确保能上网。

然后安装 dhcp 的客户端。

```Shell
sudo apt-get update
sudo apt-get install dhcpcd5
```

之后在终端中运行一次 dhcpcd5

```Shell
dhcpcd5
```

之后再我们直接修改 /etc/network/interfaces 关于eth0的配置，使能无线dhcp上网。

重启系统，就能上网啦。
---
layout: post
title: linux container（lxc）安装及使用
date: 2019-10-13
author: zoe
tags: tools
---

# linux container（lxc）安装及使用

## 1.安装

```Shell
$ sudo apt-get install lxc lxc-templates wget bridge-utils
```

安装完成后查看配置情况，如果每个状态都是enabled，则表示当前环境支持LXC。

```Shell
$ lxc-checkconfig

Kernel configuration not found at /proc/config.gz; searching...
Kernel configuration found at /boot/config-4.10.0-33-generic
--- Namespaces ---
Namespaces: enabled
Utsname namespace: enabled
Ipc namespace: enabled
Pid namespace: enabled
User namespace: enabled
Warning: newuidmap is not setuid-root
Warning: newgidmap is not setuid-root
Network namespace: enabled

--- Control groups ---
Cgroup: enabled
Cgroup clone_children flag: enabled
Cgroup device: enabled
Cgroup sched: enabled
Cgroup cpu account: enabled
Cgroup memory controller: enabled
Cgroup cpuset: enabled

...
```

## 2.使用默认模板创建新的container

查看当前可以用的模板：

```Shell
$ ls /usr/share/lxc/templates/
lxc-alpine    lxc-archlinux  lxc-centos  lxc-debian    lxc-fedora  lxc-openmandriva  lxc-oracle  lxc-slackware   lxc-sshd    lxc-ubuntu-cloud
lxc-altlinux  lxc-busybox    lxc-cirros  lxc-download  lxc-gentoo  lxc-opensuse      lxc-plamo   lxc-sparclinux  lxc-ubuntu
```

利用可用的模板创建一个ubuntu的容器

```ruby
$ sudo lxc-create -n demo -t ubuntu
```

这条命令中

- -n 后面的参数是新创建的container的名字
- -t 后面的参数是创建container所用模板的名字
- -r 模板脚本参数，表示ubunu发行版本号

创建完成后，利用工具lxc-ls可以查看当前建立的container

```Shell
$ sudo lxc-ls
centos_lxc sshd-lxc demo
```

只有root才有权限，新建立的container的文件系统保存在目录`/var/lib/lxc//rootfs`下面，同时还有一个配置文件config

```php
$ cat config
# Template used to create this container: /usr/share/lxc/templates/lxc-centos
# Parameters passed to the template: -R 7 -a x86_64
# Template script checksum (SHA-1): 85868977b29d63f5ada56fd0d3a138854d0b5eff
# For additional config options, please look at lxc.container.conf(5)

# Uncomment the following line to support nesting containers:
#lxc.include = /usr/share/lxc/config/nesting.conf
# (Be aware this has security implications)

lxc.network.type = veth
lxc.network.link = lxcbr0
lxc.network.hwaddr = fe:e9:10:40:1a:93
lxc.network.flags = up
lxc.rootfs = /var/lib/lxc/centos_lxc/rootfs
lxc.rootfs.backend = dir

# Include common configuration
lxc.include = /usr/share/lxc/config/centos.common.conf

lxc.arch = x86_64
lxc.utsname = demo

# When using LXC with apparmor, uncomment the next line to run unconfined:
#lxc.aa_profile = unconfined

# example simple networking setup, uncomment to enable
#lxc.network.type = veth
#lxc.network.flags = up
#lxc.network.link = lxcbr0
#lxc.network.name = eth0
# Additional example for veth network type
#    static MAC address,
#lxc.network.hwaddr = 00:16:3e:77:52:20
#    persistent veth device name on host side
#        Note: This may potentially collide with other containers of same name!
#lxc.network.veth.pair = v-centos_lxc-e0
```

## 3.开启容器中的机器

```Shell
$ sudo lxc-start –n demo
```

- lxc-info
  查看某一个正在运行的container的详细信息

```Shell
$ lxc-info -n demo
Name:           demo
State:          RUNNING
PID:            4139
IP:             10.0.3.33
CPU use:        0.87 seconds
...
```

- lxc-stop
  停止一个container

```Shell
$ lxc-stop -n demo
```

- lxc-console
  进入一个container的控制台

```Shell
$ lxc-console -n demo
```

- lxc-ls
  查看container的详细信息

```Shell
$ lxc-ls -f
NAME       STATE   AUTOSTART GROUPS IPV4      IPV6
demo       RUNNING 0         -      10.0.3.33 -
sshd-lxc   STOPPED 0         -      -         -
ubuntu_lxc STOPPED 0         -      -         -

```

## 4.Clone Container

从一个已经创建好的container克隆出一个新的来

```php
$ lxc-clone -n centos_lxc -N centos_server
```

查看克隆好的新的lxc container

```ruby
$ lxc-ls 
centos_client centos_lxc    centos_server sshd-lxc      ubuntu_lxc
```

### 给container分配资源

修改config文件，通过添加一行配置修改cpu分配，例如分配了CPU 0给container

```undefined
lxc.cgroup.cpuset.cpus = 0
```

### 在主机和container之间共享文件夹

首先在container内部创建一个文件夹，比如说`/mnt/share`

```ruby
$ mkdir /mnt/share
```

然后主机上也创建一个文件夹，比如说'/tmp/share'

```ruby
$ mkdir /tmp/share
```

这个时候主机上保存container文件系统的目录下面也会产生`/mnt/share`这个目录，找到这个目录的绝对路径
修改container的配置文件config， 添加一行

```jsx
lxc.mount.entry = /tmp/share /var/lib/lxc/centos_client/rootfs/mnt/share none bind 0 0
```
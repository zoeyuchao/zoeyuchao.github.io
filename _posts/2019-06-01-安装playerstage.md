---
layout: post
title: 安装player/stage
data: 2019-06-11
author: zoe
tags: tools
---

# 安装player/stage

## 1. player

```Shell
$ git clone https://github.com/playerproject/player
$ cd player
$ mkdir build
$ cd build
$ cmake -jn -DBUILD_PYTHONCPP_BINDINGS=ON ..
$ sudo make install -jn
```

遇到错误 /usr/bin/ld: cannot find -lgeos 解决方案如下，没有++不好用，因为这是c++的语言。

```Shell
sudo apt-get install libgeos++-dev
```

## 2.stage

```Shell
$ git clone https://github.com/rtv/Stage
$ cd Stage
$ mkdir build
$ cd build
$ cmake -jn ..
$ sudo make install -jn
```


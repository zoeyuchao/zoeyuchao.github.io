---
layout: post
title: Anaconda安装opencv显示图片报错
date: 2019-01-07
author: 余老板
tags: 调试笔记
---

# Anaconda安装opencv显示图片报错

 
## 错误描述

用conda 在 python3.7 环境下 安装 opencv 后。用opencv显示图片经常出现以下错误：

```Text
cv2.imshow("Original",I)
cv2.error: /io/opencv/modules/highgui/src/window.cpp:583: error: (-2) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Carbon support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function cvShowImage
```

## 原因分析

这个原因是 conda 自己编译的 opencv 库没有编译显示相关的功能，或者与环境中自己装的opencv有冲突。

## 解决方案

如果已经安装了 conda 的 opencv，就需要卸载原来的 conda 中的 opencv。（为了不影响别人的环境，建议使用conda的虚拟环境）

```Shell
conda remove opencv
```

从 menpo 安装

```Shell
conda install -c menpo opencv3
```
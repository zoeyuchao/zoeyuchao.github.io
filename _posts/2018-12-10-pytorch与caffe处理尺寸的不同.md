---
layout: post
title: pytorch与caffe处理尺寸的不同
date: 2018-12-10
author: 阿金
tags: 深度学习
---

# pytorch与caffe处理尺寸的不同

## 现象描述

发现 poolingsize 和 stride 配合起来有余头的时候，pytroch和caffe的处理方式不同。

比如 4x4 的 feature map， kernelsize = 3x3, stride = 2，的pooling。pytroch 输出尺寸是 1x1。caffe 输出尺寸是 2x2。

这个问题，导致pytorch模型向caffe模型转化的时候存在问题。

## 解决思路

我还没想好。

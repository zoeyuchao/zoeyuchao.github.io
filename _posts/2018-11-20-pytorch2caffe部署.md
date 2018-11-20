---
layout: post
title: pytorch2caffe项目的部署
date: 2018-11-20
author: 阿金
tags: 深度学习
---

# pytorch2caffe项目的部署

我用pytorch定义了一个网络，并且可以训练该网络。为了在DPU上操作，我需要把pytorch的模型转化成为caffemodel。

我现在默认我们已经能够运行 pytorch了。 其中 conda 的虚拟环境名称为 pth4。

## 开源项目

现在有一个开源项目可以搞定这个事情。

```Git
git clone https://github.com/longcw/pytorch2caffe.git
```

在readme中尝试使用方法非常简单。直接用 conda 修复需要的库就可以运行啦。

## 直接运行出错

直接运行 上述开源项目中 README 中的 Demo。
会报错。

```Shell
KeyError: ‘ExpandBackward
```

这是由于该项目用的是老版本pytorch0.2，我们运行的是新版本pytorch，导致网络表述不同。

对此我们需要安装老版本 pytorch0.2。

```Shell
conda create -n pytorch2caffe python=2.7 #新建虚拟环境
conda activate pytorch2caffe #激活虚拟环境
conda install pytorch=0.2.0 torchvision=0.1.8 #在该虚拟环境下安装对应版本的pytorch和torchvision
conda install caffe matplotlib pydot graphviz #安装依赖库
pip install graphviz
```

一定需要在conda 虚拟环境 pth4 中运行指令 ``` pip graphviz ``` 来安装 graphviz 库。

之后，就可以运行啦。

## 新老模型不兼容

然而，运行模型转换的时候，由于我们的模型是新版本pytorch生成的，转换却用的老版本pytorch。导致老版本无法读取新版本的网络参数。会报错。

```Shell
‘module’ object has no attribute ‘_rebuild_tensor_v2’
```

这时不要慌，在你加载新版本网络参数的时候，在python脚本起始几行添加如下代码。自己定义 _rebuild_tensor_v2 函数。

```Python
import torch._utils
try:
    torch._utils._rebuild_tensor_v2
except AttributeError:
    def _rebuild_tensor_v2(storage, storage_offset, size, stride, requires_grad, backward_hooks):
        tensor = torch._utils._rebuild_tensor(storage, storage_offset, size, stride)
        tensor.requires_grad = requires_grad
        tensor._backward_hooks = backward_hooks
        return tensor
    torch._utils._rebuild_tensor_v2 = _rebuild_tensor_v2
```

如此之后，便可成功运行。
---
layout: post
title: knock knock使用记录
date: 2019-04-08
author: zoe
tags: tools
---

# knock knock使用记录

> 小型的代码库 Knock Knock，当你的模型训练完成或者训练过程出现问题时，它会及时通知你。而你只需要写两行代码。

代码传送门：[https://github.com/huggingface/knockknock](http://link.zhihu.com/?target=https%3A//github.com/huggingface/knockknock)

在训练[深度学习](http://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s%3F__biz%3DMzA3MzI4MjgzMw%3D%3D%26mid%3D2650759544%26idx%3D3%26sn%3D0a669b690183b954118da0158881effd%26chksm%3D871aa506b06d2c10159e8e251cc56b7dcb5a940cec77ea7e0c00488498fc83a1ba47a6fd8bc9%26token%3D991947199%26lang%3Dzh_CN)模型时，我们通常会使用早停法。除了粗略的估计，你很难预测出训练什么时候会结束。因此，为模型训练设置自动通知就很有意思了。而且当训练因为未知原因而中途崩溃时，收到通知就更重要了。

## 1. 安装

```Shell
pip install knockknock
或者
conda install -c victorsanh knockknock
```

**该代码仅用 Python3.6 测试过。**

## 2. 使用

该库可无缝使用，只需对代码做最小的修改：你只需在主函数调用上加一个装饰器。

现在有三种设置通知的方式：邮件、 Slack、telegram。显然邮件会是我采用的方式，然而没网的时候不大好使，搞了个slack试一下。

**1.邮件**

邮件服务要依赖 Yagmail，这是一个 GMAIL/SMTP 客户端。你需要一个 gmail 邮件地址来使用它。最好创建一个新的邮件地址（不要使用常用地址），因为你需要修改账户的安全设置，以允许该 Python 库打开不太安全的 APP（选中 Allow less secure apps）进而访问它。

```Shell
from knockknock import email_sender
@email_sender(recipient_email: "<your_email@address.com>", sender_email: "<grandma's_email@gmail.com>")def train_your_nicest_model(your_nicest_parameters):
    import time
    time.sleep(10000)
```

如果未指定 sender_email，则 recipient_email 也可以用于发送邮件。

注意，启用此功能会向你询问发件人的邮箱密码。密码将通过 keyring Python 库被安全地存储在系统 keyring 服务中。

**2.Slack**

你还可以使用 slack 来获取通知。你必须提交 Slack 房间的 webhook URL 和用户 id（用户 id 为可选项，如果你想添加自己或其他人则选择该项）

https://api.slack.com/incoming-webhooks#create_a_webhook 在这个链接里把自己需要的channel授权，会生成新的url

```Shell
from knockknock import slack_sender

webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
@slack_sender(webhook_url=webhook_url, channel="train", user_mentions=["zoeyuchao"])
def train_your_nicest_model(your_nicest_parameters):
    import time
    time.sleep(10)
    
train_your_nicest_model(1)
```

你还可以指定一个可选参数来添加特定的人：user_mentions=[<your_slack_id>, <grandma's_slack_id>]。
---
layout: post
title: Weights & Biases使用指南
date: 2020-10-15
author: zoe
tags: tools
---

# Weights & Biases使用指南

[Weights & Biases](https://www.wandb.com/) 简单来说就是进阶版的tensorboard，功能更加强大，如果要详细说它跟tensorboard有什么不同，参考官网的这一段[解释](https://docs.wandb.com/library/technical-faq)。附图如下：

![compare](https://github.com/zoeyuchao/zoeyuchao.github.io/tree/master/img/compare.png)

我个人比较看中的是W&B能够帮助我记录实验的参数（甚至详细到git commit，防止自己又跑错了实验==），并且具有group功能，直接画出RL需要的均值方差图。另外第4点和第5点也是促使我使用它的重要原因。

那么接下来详细说一说怎么使用W&B，官网有[guide](https://docs.wandb.com/)，写得很好，这里总结一个简单的入门版本，供参考。

## 1.安装

W&B 支持python3和python2，我貌似都试过，还是python3支持的好一些，所以建议conda create一个python3的环境，然后执行

```Bash
pip install wandb
```

## 2. login

这一步为什么叫login呢，因为我们可以有2种方式来使用W&B，一种是使用云端，也就是这家公司提供的cloud服务，可以申请一个个人[免费账户](https://wandb.ai/login?signup=true)，然后执行

```Bash
wandb login --host=https://api.wandb.ai
```

按照他的提示去拿到API Key即可。

但是，可能会有网络问题，比如我经常传不上去files，程序就会卡住，以及数据安全问题。还有一种方案，就是找一台电脑搭建local server，如何搭建local[参考链接](https://docs.wandb.com/self-hosted/local)，如果你按照这里的操作搭建完一切正常，那么你运气超级好，恭喜你！但是，更经常的是会遇到打不开localhost:8080的问题，不要慌，我们探索到了[解决方案](https://github.com/wandb/client/issues/1054)，如下：

```Bash
docker exec -it wandb-local bash
sudo mysql
use wandb_local
SELECT * FROM schema_migrations;
```
不停地执行最后一句，直到它返回的dirty=0，那么恭喜你，local server启动好了。然后执行：

```Bash
wandb login --host=https://xxxxx:8080
```

这里的xxxx就是你的local server的ip。按照提示操作，同样获取API Key就可以了。

当然，我们的确可以偶尔云端跑，偶尔local跑，只要每次跑之前运行一下你到底要login到哪里去，你跑完的数据就会自动传到你login的地方去。

## 3.Run

首先我们需要更新一下我们的代码，参考这个[链接](https://docs.wandb.com/library/init)，如果觉得太长不想看，那么参考下面这个写法：

```Bash
run = wandb.init(config=args, 
                  project=args.env_name,
                  name=str(args.algorithm_name) + "_seed" + str(seed),
                  group=args.scenario_name,
                  dir=str(model_dir),
                  job_type="training",
                  reinit=True)
wandb.log({"value_loss": value_loss}, step=total_num_steps)
run.finish()
```

日常使用的话，这些就够了。

注意：

1. 我们看group图的时候，应该用mean和std dev。

2. 还可以探索一下report功能，团队协作的时候很好用。
3. 数据可以导出，支持png和csv，也就是我们可以把想要的数据导出，然后画自己想要的plot风格。

## 4. Sweep

W&B 还支持sweep，但是**注意**，我发现用了sweep之后显存无法释放【截止到20201015，已经在github上report issue了】，确实可以手动释放显存，除了略显愚蠢之外，就也还好。手动释放显存的命令参考如下：

```Bash
sudo ps -ef | grep train | grep -v grep | cut -c 9-15 | xargs kill -9
```

20201016想到了一个更加智能的方案来解决显存问题，因为我发现它的PPID会变成1，因为wandb父进程已经被kill了：

```Bash
ps -A -ostat,ppid,pid,cmd | grep -E "train|multiprocessing" | grep -v grep | awk '$2==1 {print $3}' | xargs kill -9
```

如何使用sweep呢？官网[文档指路](https://docs.wandb.com/sweeps)，下面是太长不看版本：

1. 创建一个yaml文件，更多的config[参见](https://docs.wandb.com/sweeps/configuration)

   ```Bash
   program: train/train_mpe.py
   project: sweep_MPE
   name: simple_spread_mlp
   command:
     - ${env}
     - python3
     - ${program}
     - --recurrent_policy
     - ${args}
   method: grid
   metric:
     goal: maximize
     name: average_episode_rewards
   parameters:
     env_name:
       distribution: constant
       value: "MPE"
     scenario_name:
       distribution: constant
       value: "simple_spread"
     algorithm_name:
       distribution: constant
       value: "hyper_sweep"
     num_agents:
       distribution: constant
       value: 3
     num_landmarks:
       distribution: constant
       value: 3
     seed:
       distribution: constant
       value: 1
     n_rollout_threads:
       distribution: constant
       value: 128
     data_chunk_length:
       distribution: constant
       value: 10
     num_env_steps:
       distribution: constant
       value: 10000000
     episode_length:
       distribution: constant
       value: 25
     num_mini_batch:
       distribution: constant
       value: 1 
     gain:
       distribution: constant
       value: 0.01
     lr:
       distribution: categorical
       values: [0.01, 0.001, 0.0001, 0.0005, 0.0007]
     ppo_epoch:
       distribution: categorical
       values: [10, 25]
   ```

2. 创建一个sweep id

   ```Bash
   wandb sweep sweep.yaml
   ```

3. 开启sweep agent

    ```Bash
    wandb agent your-sweep-id
    ```

如果sweep结束了，你发现有一些东西需要重跑，那么要先删掉它们相关的文件，有run文件还有config文件，local和server端都删掉。然后在server上**resume sweep id**，本地继续执行wandb agent命令，他就会自己跑剩下的实验。
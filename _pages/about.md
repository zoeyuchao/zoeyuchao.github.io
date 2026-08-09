---
permalink: /
title: "Chao Yu - Homepage"  
excerpt: "Ph.D student in NERC at Peking University. Research focus on AI for Life Science & NeuroAI."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
header:
  og_image: images/profile.png       # 【关键】告诉 Google 搜索和微信分享用这张图
  teaser: images/profile.png         # 站内缩略图
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

My name is <span class="accent-text">Chao Yu（于超）</span>. I received my Ph.D. from the Department of Electronic Engineering at **Tsinghua University**<img src='images/thulogo.png' style="height:1em; vertical-align:middle;"> in 2023. I am currently an Assistant Professor (Distinguished Research Fellow) at the <a href="https://thusigs-edi-lab.github.io" class="link-accent">Embodied Decision Intelligence Lab (EDI Lab)</a> at **Tsinghua Shenzhen International Graduate School (SIGS)**<img src='images/sigs.png' style="height:1em; vertical-align:middle;">. I also serve as the chairman of the **Tsinghua Shenzhen International Graduate School - AgiBot Joint Research Center for Embodied Cognition and Decision Systems (JCES)** 清华-智元联合研究中⼼主任. I'm also the **co-founder of Striding AI(正行创新)**. I have been selected for the **Youth Talent Support Program** of the Chinese Institute of Electronics. My research has long focused on **reinforcement learning–based decision intelligence**. As first author or corresponding author, I have published more than 50 papers in top-tier international conferences and journals, including ICML, NeurIPS, ICLR, CVPR, ECCV, CoRL, IROS, ICRA, TMLR, and RAL, with over 7,000 citations on Google Scholar. My representative works include the multi-agent reinforcement learning algorithm<a href="https://github.com/marlbenchmark/on-policy" class="link-accent"> **MAPPO**</a>, which has received more than 4,000 Google Scholar citations, and<a href="https://github.com/RLinf/RLinf" class="link-accent"> **RLinf**</a>, a large-scale reinforcement learning training framework for embodied intelligence, which has accumulated over 4,000 GitHub stars.

Feel free to reach out if you'd like to discuss research or explore potential collaboration!

# 📃 Research Interest
<div class="highlight-blocks">
  <div class="highlight-block floating-card">
    <h3><i class="fas fa-microscope"></i> RL Infra</h3>
    <ul>
      <li>My <span class="primary-gradient-text">Technical Preference</span>: 
        Scalable reinforcement learning systems, training infrastructure, and system-algorithm co-design for large-scale policy optimization.
      </li>
      <li>Representative works on <span class="primary-gradient-text">RL Infra</span> include: 
        <a href="https://github.com/RLinf/RLinf" class="link-accent"> RLinf</a> and etc.
        covering efficient RL training, real-world online policy learning, and VLA+RL system design.
      </li>
    </ul>
  </div>
  
  <div class="highlight-block floating-card">
    <h3><i class="fas fa-pen-fancy"></i> Strategic Agent</h3> 
    <ul>
      <li>
        My <span class="primary-gradient-text">Research Focus</span>: 
        multi-agent RL, strategic reasoning, self-play, cooperation/competition, and language agents.
      </li>
      <li>
        Representative works include 
        <a href="https://github.com/marlbenchmark/on-policy" class="link-accent"> MAPPO</a>,
        <a href="https://arxiv.org/abs/2310.03354" class="link-accent"> Fictitious Cross-Play</a>,
        <a href="https://arxiv.org/abs/2510.15414" class="link-accent"> MARSHAL</a>,
        <a href="https://arxiv.org/abs/2602.04634" class="link-accent"> WideSeek-R1</a>,
        <a href="https://arxiv.org/abs/2502.04686" class="link-accent"> Werewolf game</a> etc.
      </li>
    </ul>
  </div>
  
  <div class="highlight-block floating-card">
    <h3><i class="fas fa-globe-asia"></i> Embodied Agent</h3>
    <ul>
      <li>My <span class="primary-gradient-text">Application Interest</span>: 
        embodied intelligence with quadrupeds, drones, multi-robot systems, VLA models, and world-model-based robotic training.
      </li>
      <li>Representative works include
        <a href="https://arxiv.org/abs/2602.13977" class="link-accent"> WoVR</a>,
        <a href="https://arxiv.org/abs/2510.25889" class="link-accent"> πRL</a>,
        <a href="https://arxiv.org/abs/2509.19080" class="link-accent"> World4RL</a>,
        <a href="https://arxiv.org/abs/2512.03556" class="link-accent"> RoboScape-R</a>,
        <a href="https://sites.google.com/view/thu-volleybots" class="link-accent"> VolleyBots</a>,
        <a href="https://arxiv.org/abs/2406.05687" class="link-accent"> FlightBench</a>,
        <a href="https://github.com/btx0424/OmniDrones" class="link-accent"> OmniDrones</a>,
        and etc.
      </li>
    </ul>
  </div>
</div>

<span class='anchor' id='-educations'></span>
# 🏫 Educations

- *2019 - 2023*: &nbsp;**Department of Electronic Engineering, Tsinghua University**<img src='images/thulogo.png' style="height:1em; vertical-align:middle;">.  
  &nbsp;&nbsp;Ph.D. in Electronic Science and Technology.  
  &nbsp;&nbsp;*Outstanding Doctoral Graduate (Top 5%), Outstanding Doctoral Thesis (Top 10%)*.  
  &nbsp;&nbsp;Advisor: <a href="https://web.ee.tsinghua.edu.cn/wangyu/zh_CN/index.htm" class="link-accent">Prof. Yu Wang</a>; Co-advisor: <a href="https://jxwuyi.weebly.com/" class="link-accent">Assistant Prof. Yi Wu</a>.

- *2016 - 2019*: &nbsp;**Department of Mechanical Engineering, Tsinghua University**<img src='images/thulogo.png' style="height:1em; vertical-align:middle;">.  
  &nbsp;&nbsp;M.S. in Mechanical Engineering and Automation.  
  &nbsp;&nbsp;*Outstanding Master's Thesis (Top 10%)*.  
  &nbsp;&nbsp;Advisor: <a href="https://www.me.tsinghua.edu.cn/info/1091/3535.htm" class="link-accent">Prof. Xin-Jun Liu</a>.

- *2012 - 2016*: &nbsp;**School of Automation, Beijing Institute of Technology**<img src='images/bitlogo.png' style="height:1em; vertical-align:middle;">.  
  &nbsp;&nbsp;B.S. in Automation.  
  &nbsp;&nbsp;*Outstanding Graduate (Top 15%)*.


<span class='anchor' id='-publications'></span>
# 📃 Publications

<div id="publications-wrapper">
  <div id="filter-container"></div>

  <div class='paper-box floating-card' data-tags="2027, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">NSDI 2027</div>
    <img src='images/fusco.png' alt="FUSCO Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>FUSCO: High-Performance Distributed Data Shuffling via Transformation-Communication Fusion</h3>
    <div class="authors">Zhuoran Zhu, Chunyang Zhu, Hao Lin, Xu Fu, Yiming Zhou, Quanlu Zhang, Zhenhua Li, Feng Qian, <span class="primary-gradient-text">Chao Yu</span>, Boxun Li, Guohao Dai, Yu Wang</div>
    <div class="venue">24th USENIX Symposium on Networked Systems Design and Implementation (NSDI 2027)</div>
<div class="links">
  <a href="https://arxiv.org/pdf/2512.22036" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
</div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2026, Journal, CCF-B">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">RA-L 2026</div>
      <img src='images/Human-Guided.png' alt="Human-Guided Online Reward Adaptation Overview" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Human-Guided Online Reward Adaptation for Real-Robot Arm Manipulation</h3>
      <div class="authors">Tianxing Zhou, Haojia Ao, Haoyang Lu, Guangyan Chen, Zichen Zhou, Te Cui, <span class="primary-gradient-text">Chao Yu</span>, Yufeng Yue📧</div>
      <div class="venue">IEEE Robotics and Automation Letters (RA-L 2026)</div>
      <div class="links"></div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2025, Journal">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">RA-L 2025</div>
    <img src='images/zeroshotstudy.png' alt="Zero-Shot Sim-to-Real RL Study Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>What Matters in Learning A Zero-Shot Sim-to-Real RL Policy for Quadrotor Control? A Comprehensive Study</h3>
    <div class="authors">Jiayu Chen⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️📧, Yuqing Xie, Feng Gao, Yinuo Chen, Shu'ang Yu, Wenhao Tang, Shilong Ji, Mo Mu, Yi Wu, Huazhong Yang, Yu Wang📧</div>
    <div class="venue">IEEE Robotics and Automation Letters (RA-L 2025)</div>
<div class="links">
  <a href="https://arxiv.org/abs/2412.11764" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
</div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2026, Conference, CCF-C">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">RLC 2026</div>
      <img src='images/icpl.png' alt="ICPL Overview" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>ICPL: Few-shot In-Context Preference Learning via LLMs</h3>
      <div class="authors"><span class="primary-gradient-text">Chao Yu</span>⭐️, Qixin Tan⭐️, Hong Lu, Jiaxuan Gao, Xinting Yang, Yu Wang, Yi Wu, Eugene Vinitsky📧</div>
      <div class="venue">Reinforcement Learning Conference (RLC 2026)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2410.17233" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">OSDI 2026</div>
      <img src='images/dynarl.png' alt="DynaRL Overview" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>DynaRL: Flexible and Dynamic Scheduling of Large-Scale Reinforcement Learning Training</h3>
      <div class="authors">Yuanqing Wang, Hao Lin, Junhao Hu, Chunyang Zhu, Quanlu Zhang, Zhen Guo, Yuchen Zhang, Xu Fu, Si Xu, Bo Dai, Zixiao Huang, <span class="primary-gradient-text">Chao Yu</span>, Boxun Li, Guohao Dai, Zhi Yang, Yu Wang</div>
      <div class="venue">20th USENIX Symposium on Operating Systems Design and Implementation (OSDI 2026)</div>
      <div class="links">
        <a href="https://www.usenix.org/conference/osdi26/presentation/wang-yuanqing" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>
  
  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">ACM MM 2026</div>
      <img src='images/tex3d.png' alt="Tex3D Overview" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models</h3>
      <div class="authors">Jiawei Chen, Simin Huang, Jiawei Du, Shuaihang Chen, Yu Tian, Mingjie Wei, <span class="primary-gradient-text">Chao Yu</span>📧, Zhaoxia Yin📧</div>
      <div class="venue">ACM International Conference on Multimedia (ACM MM 2026)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2604.01618" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
        <a href="https://vla-attack.github.io/tex3d/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Preprint">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">arXiv 2026</div>
      <img src='images/wovr.png' alt="WoVR" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL</h3>
      <div class="authors">Zhennan Jiang, Shangqing Zhou, Yutong Jiang, Zefang Huang, Mingjie Wei, Yuhui Chen, Tianxing Zhou, Zhen Guo, Hao Lin, Quanlu Zhang, Yu Wang, Haoran Li📧, <span class="primary-gradient-text">Chao Yu</span>📧, Dongbin Zhao</div>
      <div class="venue">arXiv preprint arXiv:2602.13977 (2026)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2602.13977" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Preprint">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">arXiv 2026</div>
      <img src='images/beyondlim.png' alt="Beyond Imitation" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models</h3>
      <div class="authors">Liangzhi Shi⭐️, Shuaihang Chen⭐️, Feng Gao, Yinuo Chen, Kang Chen, Tonghe Zhang, Hongzhi Zang, Weinan Zhang, <span class="primary-gradient-text">Chao Yu</span>, Yu Wang</div>
      <div class="venue">arXiv preprint arXiv:2602.12628 (2026)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2602.12628" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">RSS 2026</div>
      <img src='images/rlinfuser.png' alt="RLinf-USER" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>USER: A Unified and Extensible System for Real-World Online Policy Learning in Embodied AI</h3>
      <div class="authors">Hongzhi Zang⭐️, Shu'ang Yu⭐️, Hao Lin, Tianxing Zhou, Zefang Huang, Zhen Guo, Xin Xu, Jiakai Zhou, Yuze Sheng, Shizhe Zhang, Feng Gao, Wenhao Tang, Yufeng Yue, Quanlu Zhang, Xinlei Chen, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
      <div class="venue">Robotics: Science and Systems (RSS 2026)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2602.07837" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Preprint">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">arXiv 2026</div>
    <img src='images/wideseek.png' alt="WideSeek-R1 Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning</h3>
    <div class="authors">Zelai Xu⭐️, Zhexuan Xu⭐️, Ruize Zhang⭐️, Chunyang Zhu, Shi Yu, Weilin Liu, Quanlu Zhang, Wenbo Ding, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
    <div class="venue">arXiv preprint (2026)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2602.04634" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">CVPR 2026</div>
    <img src='images/roboscape.png' alt="RoboScape-R Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>RoboScape-R: Unified Reward-Observation World Models for Generalizable Robotics Training via RL</h3>
    <div class="authors">Yinzhou Tang, Yu Shang, Yinuo Chen, Bingwen Wei, Xin Zhang, Shu'ang Yu, Liangzhi Shi, <span class="primary-gradient-text">Chao Yu</span>, Chen Gao, Wei Wu, Yong Li</div>
    <div class="venue">IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026), Findings</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2512.03556" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ACL 2025</div>
    <img src='images/redteam.png' alt="Red Teaming Large Reasoning Models Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Red Teaming Large Reasoning Models</h3>
    <div class="authors">Jiawei Chen⭐️, Yang Yang⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️, Yu Tian, Zhi Cao, Xue Yang, Linghao Li, Hang Su, Zhaoxia Yin📧</div>
    <div class="venue">Annual Meeting of the Association for Computational Linguistics (ACL 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2512.00412" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Preprint">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">arXiv 2025</div>
    <img src='images/pirl.png' alt="piRL Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models</h3>
    <div class="authors">Kang Chen⭐️, Zhihao Liu⭐️, Tonghe Zhang⭐️, Zhen Guo, Si Xu, Hao Lin, Hongzhi Zang, Quanlu Zhang, Zhaofei Yu, Guoliang Fan, Tiejun Huang, Yu Wang📧, <span class="primary-gradient-text">Chao Yu</span>📧</div>
    <div class="venue">arXiv preprint arXiv:2510.25889 (2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2510.25889" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

  <div class='paper-box floating-card' data-tags="2025, Conference, CCF-B">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">IROS 2025</div>
      <img src='images/longhorizon.png' alt="Long-horizon quadruped" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Long-horizon Locomotion and Manipulation on a Quadrupedal Robot with Large Language Models</h3>
      <div class="authors">Yutao Ouyang, Jinhan Li, Yunfei Li, Zhongyu Li, <span class="primary-gradient-text">Chao Yu</span>, Koushil Sreenath, Yi Wu</div>
      <div class="venue">IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2404.05291" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICLR 2026</div>
    <img src='images/marshal.png' alt="MARSHAL Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs</h3>
    <div class="authors">Huining Yuan⭐️, Zelai Xu⭐️, Zheyue Tan, Xiangmin Yi, Mo Guang, Kaiwen Long, Haojia Hui, Boxun Li, Xinlei Chen, Bo Zhao, Xiao-Ping Zhang📧, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
    <div class="venue">International Conference on Learning Representations (ICLR 2026)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2510.15414" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">RSS 2026</div>
      <img src='images/rlinfvla.png' alt="RLinf-VLA" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models</h3>
      <div class="authors">Hongzhi Zang, Mingjie Wei, Si Xu, Yongji Wu, Zhen Guo, Yuanqing Wang, Hao Lin, Liangzhi Shi, Yuqing Xie, Zhexuan Xu, Zhihao Liu, Kang Chen, Wenhao Tang, Quanlu Zhang, Weinan Zhang, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
      <div class="venue">Robotics: Science and Systems (RSS 2026)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2510.06710" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">ICLR 2026</div>
      <img src='images/sacflow.png' alt="SAC Flow" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>SAC Flow: Sample-Efficient Reinforcement Learning of Flow-Based Policies via Velocity-Reparameterized Sequential Modeling</h3>
      <div class="authors">Yixian Zhang⭐️, Shu'ang Yu⭐️, Tonghe Zhang, Mo Guang, Haojia Hui, Kaiwen Long, Yu Wang, <span class="primary-gradient-text">Chao Yu</span>📧, Wenbo Ding📧</div>
      <div class="venue">International Conference on Learning Representations (ICLR 2026)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2509.25756" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICLR 2026</div>
    <img src='images/repo.png' alt="RE-PO Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>RE-PO: Robust Enhanced Policy Optimization as a General Framework for LLM Alignment</h3>
    <div class="authors">Xiaoyang Cao⭐️, Zelai Xu⭐️, Mo Guang, Kaiwen Long, Michiel A. Bakker, Yu Wang📧, <span class="primary-gradient-text">Chao Yu</span>📧</div>
    <div class="venue">International Conference on Learning Representations (ICLR 2026)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2509.24159" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">ICRA 2026</div>
      <img src='images/jugglerl.png' alt="JuggleRL" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>JuggleRL: Mastering Ball Juggling with a Quadrotor via Deep Reinforcement Learning</h3>
      <div class="authors">Shilong Ji, Yinuo Chen, Chuqi Wang, Jiayu Chen, Ruize Zhang, Feng Gao, Wenhao Tang, Shu'ang Yu, Sirui Xiang, Xinlei Chen, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
      <div class="venue">IEEE International Conference on Robotics and Automation (ICRA 2026)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2509.24892" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Journal, CCF-B">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">RA-L 2026</div>
      <img src='images/world4rl.png' alt="World4RL" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation</h3>
      <div class="authors">Zhennan Jiang, Kai Liu, Yuxin Qin, Shuai Tian, Yupeng Zheng, Mingcai Zhou, <span class="primary-gradient-text">Chao Yu</span>📧, Haoran Li📧, Dongbin Zhao</div>
      <div class="venue">IEEE Robotics and Automation Letters (RA-L 2026)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2509.19080" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">OSDI 2026</div>
    <img src='images/rlinf.png' alt="RLinf Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>, Yuanqing Wang, Zhen Guo, Hao Lin, Si Xu, Hongzhi Zang, Quanlu Zhang, Yongji Wu, Chunyang Zhu, Junhao Hu, Zixiao Huang, Mingjie Wei, Yuqing Xie, Ke Yang, Bo Dai, Zhexuan Xu, Xiangyuan Wang, Xu Fu, Zhihao Liu, Kang Chen, Weilin Liu, Gang Liu, Boxun Li, Jianlei Yang, Zhi Yang, Guohao Dai, Yu Wang📧</div>
    <div class="venue">20th USENIX Symposium on Operating Systems Design and Implementation (OSDI 2026)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2509.15965" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://github.com/RLinf/RLinf" class="btn-accent"><i class="fab fa-github"></i> Code</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2026, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">IROS 2026</div>
    <img src='images/d3p.png' alt="D3P Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning</h3>
    <div class="authors">Shu-Ang Yu, Feng Gao, Yi Wu, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
    <div class="venue">IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2026)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2508.06804" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

  <div class='paper-box floating-card' data-tags="2025, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">EMNLP 2025 Main</div>
      <img src='images/specvla.png' alt="Spec-VLA" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance</h3>
      <div class="authors">Songsheng Wang, Rucheng Yu, Zhihang Yuan, <span class="primary-gradient-text">Chao Yu</span>, Feng Gao, Yu Wang, Derek F. Wong📧</div>
      <div class="venue">Conference on Empirical Methods in Natural Language Processing (EMNLP 2025), Main Conference</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2507.22424" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2025, Journal">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">RA-L 2025</div>
      <img src='images/multiuav.png' alt="Pursuit-Evasion" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Online Planning for Multi-UAV Pursuit-Evasion in Unknown Environments Using Deep Reinforcement Learning</h3>
      <div class="authors">Jiayu Chen⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️📧, Guosheng Li, Wenhao Tang, Xinyi Yang, Botian Xu, Huazhong Yang, Yu Wang📧</div>
      <div class="venue">IEEE Robotics and Automation Letters (RA-L 2025)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2409.15866" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2025, Preprint">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">arXiv 2025</div>
      <img src='images/risks.png' alt="Secondary Risks" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>Exploring the Secondary Risks of Large Language Models</h3>
      <div class="authors">Jiawei Chen, Zhengwei Fang, Xiao Yang, <span class="primary-gradient-text">Chao Yu</span>, Zhaoxia Yin, Hang Su</div>
      <div class="venue">arXiv preprint arXiv:2506.12382 (2025)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2506.12382" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">CVPR 2026 Oral</div>
      <img src='images/vsbench.png' alt="VS-Bench" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>VS-Bench: Evaluating VLMs for Strategic Reasoning and Decision-Making in Multi-Agent Environments</h3>
      <div class="authors">Zelai Xu⭐️, Zhexuan Xu⭐️, Xiangmin Yi, Huining Yuan, Xinlei Chen, Yi Wu, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
      <div class="venue">IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2026), Oral</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2506.02387" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2025, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">NeurIPS 2025</div>
      <img src='images/rlstudy.png' alt="What Can RL Bring to VLA Generalization" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>What Can RL Bring to VLA Generalization? An Empirical Study</h3>
      <div class="authors">Jijia Liu⭐️, Feng Gao⭐️, Bingwen Wei, Xinlei Chen, Qingmin Liao, Yi Wu, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
      <div class="venue">Annual Conference on Neural Information Processing Systems (NeurIPS 2025)</div>
      <div class="links">
        <a href="https://arxiv.org/abs/2505.19789" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2025, Conference, CCF-A">
    <div class='paper-box-image'>
      <div class="badge pulse-accent">NeurIPS 2025</div>
      <img src='images/reinflow.png' alt="ReinFlow" width="100%">
    </div>
    <div class='paper-box-text'>
      <h3>ReinFlow: Fine-tuning Flow Matching Policy with Online Reinforcement Learning</h3>
      <div class="authors">Tonghe Zhang, <span class="primary-gradient-text">Chao Yu</span>📧, Sichang Su, Yu Wang</div>
      <div class="venue">Annual Conference on Neural Information Processing Systems (NeurIPS 2025)</div>
      <div class="links">
        <a href="https://papers.nips.cc/" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      </div>
    </div>
  </div>

  <div class='paper-box floating-card' data-tags="2025, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">CoRL 2025</div>
    <img src='images/soccer.png' alt="Quadrupedal Soccer Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Toward Real-World Cooperative and Competitive Soccer with Quadrupedal Robot Teams</h3>
    <div class="authors">Zhi Su⭐️, Yuman Gao⭐️, Emily Lukas, Yunfei Li, Jiaze Cai, Faris Tulbah, Fei Gao, <span class="primary-gradient-text">Chao Yu</span>, Zhongyu Li, Yi Wu, Koushil Sreenath</div>
    <div class="venue">Conference on Robot Learning (CoRL 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2505.13834" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Preprint">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">arXiv 2025</div>
    <img src='images/diffusion.png' alt="NCDPO Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Fine-tuning Diffusion Policies with Backpropagation Through Diffusion Timesteps</h3>
    <div class="authors">Ningyuan Yang, Jiaxuan Gao, Feng Gao, Yi Wu📧, <span class="primary-gradient-text">Chao Yu</span>📧</div>
    <div class="venue">arXiv preprint arXiv:2505.10482 (2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2505.10482" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">CoRL 2025</div>
    <img src='images/coselfplay.png' alt="HCSP Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Mastering Multi-Drone Volleyball through Hierarchical Co-Self-Play Reinforcement Learning</h3>
    <div class="authors">Ruize Zhang, Sirui Xiang, Zelai Xu, Feng Gao, Shilong Ji, Wenhao Tang, Wenbo Ding, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
    <div class="venue">Conference on Robot Learning (CoRL 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2505.04317" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://hi-co-self-play.github.io/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Journal">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">RA-L 2025</div>
    <img src='images/hann.png' alt="Soft Robots Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Hysteresis-Aware Neural Network Modeling and Whole-Body Reinforcement Learning Control of Soft Robots</h3>
    <div class="authors">Zongyuan Chen⭐️, Yan Xia⭐️, Jiayuan Liu, Jijia Liu, Wenhao Tang, Jiayu Chen, Feng Gao, Longfei Ma, Hongen Liao, Yu Wang, <span class="primary-gradient-text">Chao Yu</span>📧, Boyu Zhang📧, Fei Xing📧</div>
    <div class="venue">IEEE Robotics and Automation Letters (RA-L 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2504.13582" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2026, Conference, non-CCF">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">CASE 2026</div>
    <img src='images/aed.png' alt="AED Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>AED: Automatic Discovery of Effective and Diverse Vulnerabilities for Autonomous Driving Policy with Large Language Models</h3>
    <div class="authors">Le Qiu⭐️, Zelai Xu⭐️, Qixin Tan⭐️, Wenhao Tang, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
    <div class="venue">IEEE International Conference on Automation Science and Engineering (CASE 2026)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2503.20804" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://github.com/thu-nics/AED" class="btn-accent"><i class="fab fa-github"></i> Code</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Preprint">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">arXiv 2025</div>
    <img src='images/multirobot.png' alt="Multi-Robot Exploration Survey Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Multi-Robot System for Cooperative Exploration in Unknown Environments: A Survey</h3>
    <div class="authors">Chuqi Wang⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️📧, Xin Xu, Yuman Gao, Xinyi Yang, Wenhao Tang, Shu'ang Yu, Yinuo Chen, Feng Gao, ZhuoZhu Jian, Xinlei Chen, Fei Gao, Boyu Zhou, Yu Wang📧</div>
    <div class="venue">arXiv preprint arXiv:2503.07278 (2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2503.07278" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2026, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICLR 2026</div>
    <img src='images/policy2lang.png' alt="Translate Policy to Language Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Translate Policy to Language: Flow Matching Generated Rewards for LLM Explanations</h3>
    <div class="authors">Xinyi Yang, Liang Zeng, Heng Dong, <span class="primary-gradient-text">Chao Yu</span>, Xiaoran Wu, Huazhong Yang, Yu Wang, Milind Tambe, Tonghan Wang</div>
    <div class="venue">International Conference on Learning Representations (ICLR 2026)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2502.12530" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICML 2025</div>
    <img src='images/strategic.png' alt="LSPO Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization</h3>
    <div class="authors">Zelai Xu⭐️, Wanjun Gu, <span class="primary-gradient-text">Chao Yu</span>📧, Yi Wu📧, Yu Wang📧</div>
    <div class="venue">International Conference on Machine Learning (ICML 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2502.04686" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">NeurIPS 2025</div>
    <img src='images/volleybots.png' alt="VolleyBots Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>VolleyBots: A Testbed for Multi-Drone Volleyball Game Combining Motion Control and Strategic Play</h3>
    <div class="authors">Zelai Xu⭐️, Ruize Zhang⭐️, <span class="primary-gradient-text">Chao Yu</span>📧, Huining Yuan, Xiangmin Yi, Shilong Ji, Chuqi Wang, Wenhao Tang, Yu Wang📧</div>
    <div class="venue">Annual Conference on Neural Information Processing Systems (NeurIPS 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2502.01932" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://github.com/thu-uav/VolleyBots" class="btn-accent"><i class="fab fa-github"></i> Code</a>
      <a href="https://sites.google.com/view/thu-volleybots" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICML 2025</div>
    <img src='images/qnetwork.png' alt="ARSQ Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Learning from Suboptimal Data in Continuous Control via Auto-Regressive Soft Q-Network</h3>
    <div class="authors">Jijia Liu, Feng Gao, Qingmin Liao, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang📧</div>
    <div class="venue">International Conference on Machine Learning (ICML 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2502.00288" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://sites.google.com/view/ar-soft-q" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Journal">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">JMLR 2025</div>
    <img src='images/nasheqal.png' alt="GFXP Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Learning Global Nash Equilibrium in Team Competitive Games with Generalized Fictitious Cross-Play</h3>
    <div class="authors">Zelai Xu, <span class="primary-gradient-text">Chao Yu</span>📧, Yancheng Liang, Yi Wu, Yu Wang📧</div>
    <div class="venue">Journal of Machine Learning Research (JMLR 2025), Volume 26</div>
    <div class="links">
      <a href="http://www.jmlr.org/papers/v26/24-1503.html" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Conference">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">UbiComp 2024</div>
    <img src='images/sleepnet.png' alt="SleepNetZero Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>SleepNetZero: Zero-Burden Zero-Shot Reliable Sleep Staging With Neural Networks Based on Ballistocardiograms</h3>
    <div class="authors">Shuzhen Li⭐️, Yuxin Chen⭐️, Xuesong Chen, Ruiyang Gao, Yupeng Zhang, <span class="primary-gradient-text">Chao Yu</span>, Yunfei Li, Ziyi Ye, Weijun Huang, Hongliang Yi, Yue Leng, Yi Wu</div>
    <div class="venue">ACM International Conference on Ubiquitous Computing (UbiComp 2024)</div>
    <div class="links">
      <a href="https://dl.acm.org/doi/10.1145/3699743" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Journal">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">RA-L 2025</div>
    <img src='images/neuralcontrol.png' alt="NeuralIMC Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Neural Internal Model Control: Learning a Robust Control Policy via Predictive Error Feedback</h3>
    <div class="authors">Feng Gao, <span class="primary-gradient-text">Chao Yu</span>📧, Yu Wang, Yi Wu📧</div>
    <div class="venue">IEEE Robotics and Automation Letters (RA-L 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2411.13079" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://github.com/thu-uav/NeuralIMC" class="btn-accent"><i class="fab fa-github"></i> Code</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">IROS 2025</div>
    <img src='images/multiuav2.png' alt="UAV Formation Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Multi-UAV Behavior-based Formation with Static and Dynamic Obstacles Avoidance via Reinforcement Learning</h3>
    <div class="authors">Yuqing Xie⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️📧, Hongzhi Zang⭐️, Feng Gao, Wenhao Tang, Jingyi Huang, Jiayu Chen, Botian Xu, Yi Wu, Yu Wang📧</div>
    <div class="venue">IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2410.18495" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://sites.google.com/view/uav-formation-with-avoidance/" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICRA 2025</div>
    <img src='images/humanrobot.png' alt="NaviDIFF Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Human-Robot Cooperative Distribution Coupling for Hamiltonian-Constrained Social Navigation</h3>
    <div class="authors">Weizheng Wang, <span class="primary-gradient-text">Chao Yu</span>, Yu Wang, Byung-Cheol Min</div>
    <div class="venue">IEEE International Conference on Robotics and Automation (ICRA 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2409.13573" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://sites.google.com/view/NaviDIFF" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Preprint">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">arXiv 2024</div>
    <img src='images/llmrlhf.png' alt="Reward-Robust RLHF Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Reward-Robust RLHF in LLMs</h3>
    <div class="authors">Yuzi Yan, Xingzhou Lou, Jialian Li, Yiping Zhang, Jian Xie, <span class="primary-gradient-text">Chao Yu</span>, Yu Wang, Dong Yan, Yuan Shen</div>
    <div class="venue">arXiv preprint arXiv:2409.15360 (2024)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2409.15360" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Preprint">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">arXiv 2024</div>
    <img src='images/selfplaysurvey.png' alt="Self-Play Survey Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>A Survey on Self-play Methods in Reinforcement Learning</h3>
    <div class="authors">Ruize Zhang, Zelai Xu, Chengdong Ma, <span class="primary-gradient-text">Chao Yu</span>📧, Wei-Wei Tu, Shiyu Huang📧, Deheng Ye, Wenbo Ding, Yaodong Yang, Yu Wang📧</div>
    <div class="venue">arXiv preprint arXiv:2408.01072 (2024)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2408.01072" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Journal">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">RA-L 2025</div>
    <img src='images/flightbench.png' alt="FlightBench Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>FlightBench: A Comprehensive Benchmark of Spatial Planning Methods for Quadrotors</h3>
    <div class="authors">Shu-Ang Yu⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️📧, Feng Gao⭐️, Yi Wu, Yu Wang📧</div>
    <div class="venue">IEEE Robotics and Automation Letters (RA-L 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2406.05687" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">CIKM 2025</div>
    <img src='images/citylight.png' alt="CityLight Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>CityLight: A Universal Model Towards Real-world City-scale Traffic Signal Control Coordination</h3>
    <div class="authors">Jinwei Zeng, <span class="primary-gradient-text">Chao Yu</span>📧, Xinyi Yang, Wenxuan Ao, Jian Yuan, Yong Li, Yu Wang, Huazhong Yang</div>
    <div class="venue">ACM International Conference on Information and Knowledge Management (CIKM 2025)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2406.02126" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICRA 2024</div>
    <img src='images/lagoon.png' alt="LAGOON Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>LAGOON: Language-Guided Motion Control</h3>
    <div class="authors">Shusheng Xu⭐️, Huaijie Wang⭐️, Jiaxuan Gao, Yutao Ouyang, Zhiyu Mei, <span class="primary-gradient-text">Chao Yu</span>, Yi Wu</div>
    <div class="venue">IEEE International Conference on Robotics and Automation (ICRA 2024)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2306.10518" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICML 2024 Oral</div>
    <img src='images/dpostudy.png' alt="DPO vs PPO Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study</h3>
    <div class="authors">Shusheng Xu⭐️, Wei Fu⭐️, Jiaxuan Gao, Wenjie Ye, Weilin Liu, Zhiyu Mei, Guangju Wang, <span class="primary-gradient-text">Chao Yu</span>📧, Yi Wu📧</div>
    <div class="venue">International Conference on Machine Learning (ICML 2024), Oral</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2404.10719" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://github.com/openpsi-project/ReaLHF" class="btn-accent"><i class="fab fa-github"></i> Code</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">AAAI 2024</div>
    <img src='images/zerosum.png' alt="SACL Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Accelerate Multi-Agent Reinforcement Learning in Zero-Sum Games with Subgame Curriculum Learning</h3>
    <div class="authors">Jiayu Chen⭐️, Zelai Xu⭐️, Yunfei Li, <span class="primary-gradient-text">Chao Yu</span>, Jiaming Song, Huazhong Yang, Fei Fang, Yu Wang, Yi Wu</div>
    <div class="venue">AAAI Conference on Artificial Intelligence (AAAI 2024)</div>
    <div class="links">
      <a href="https://ojs.aaai.org/index.php/AAAI/article/view/29011" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://sites.google.com/view/sacl-rl" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Journal">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">RA-L 2024</div>
    <img src='images/omnidrones.png' alt="OmniDrones Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>OmniDrones: An Efficient and Flexible Platform for Reinforcement Learning in Drone Control</h3>
    <div class="authors">Botian Xu, Feng Gao, <span class="primary-gradient-text">Chao Yu</span>📧, Ruize Zhang, Yi Wu, Yu Wang📧</div>
    <div class="venue">IEEE Robotics and Automation Letters (RA-L 2024)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2309.12825" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://github.com/btx0424/OmniDrones" class="btn-accent"><i class="fab fa-github"></i> Code</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2025, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICLR 2025</div>
    <img src='images/fewshotcontext.png' alt="ICPL Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Few-shot In-context Preference Learning using Large Language Models</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>, Hong Lu, Jiaxuan Gao, Qixin Tan, Xinting Yang, Yu Wang, Yi Wu, Eugene Vinitsky</div>
    <div class="venue">International Conference on Learning Representations (ICLR 2025)</div>
    <div class="links">
      <a href="https://openreview.net/forum?id=w9tS6NRmxX" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">AAMAS 2024</div>
    <img src='images/llmpowered.png' alt="HLA Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>LLM-Powered Hierarchical Language Agent for Real-time Human-AI Coordination</h3>
    <div class="authors">Jijia Liu⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️, Jiaxuan Gao⭐️, Yuqing Xie, Qingmin Liao, Yi Wu, Yu Wang</div>
    <div class="venue">International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2024)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2312.15224" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Journal">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">RA-L 2024</div>
    <img src='images/masp.png' alt="MASP Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>MASP: Scalable Graph-based Planning towards Multi-Agent Navigation</h3>
    <div class="authors">Xinyi Yang⭐️, Xinting Yang⭐️, <span class="primary-gradient-text">Chao Yu</span>📧, Jiayu Chen, Wenbo Ding, Huazhong Yang, Yu Wang📧</div>
    <div class="venue">IEEE Robotics and Automation Letters (RA-L 2024)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2312.02522" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://sites.google.com/view/masp-ral" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2023, Journal">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">RA-L 2023</div>
    <img src='images/activeneural.png' alt="MANTM Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Active Neural Topological Mapping for Multi-Agent Exploration</h3>
    <div class="authors">Xinyi Yang⭐️, Yuxiang Yang⭐️, <span class="primary-gradient-text">Chao Yu</span>📧, Jiayu Chen, Jincheng Yu, Haibing Ren, Huazhong Yang, Yu Wang📧</div>
    <div class="venue">IEEE Robotics and Automation Letters (RA-L 2023)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2311.00252" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://sites.google.com/view/mantm" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICML 2024</div>
    <img src='images/werewolf.png' alt="Werewolf Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game</h3>
    <div class="authors">Zelai Xu, <span class="primary-gradient-text">Chao Yu</span>, Fei Fang, Yu Wang, Yi Wu</div>
    <div class="venue">International Conference on Machine Learning (ICML 2024)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2310.18940" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2023, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">AAMAS 2023</div>
    <img src='images/fictitious.png' alt="FXP Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Fictitious Cross-Play: Learning Global Nash Equilibrium in Mixed Cooperative-Competitive Games</h3>
    <div class="authors">Zelai Xu, Yancheng Liang, <span class="primary-gradient-text">Chao Yu</span>, Yu Wang, Yi Wu</div>
    <div class="venue">International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2023)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2310.03354" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2023, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">IJCAI 2023</div>
    <img src='images/truss.png' alt="AutoTruss Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Automatic Truss Design with Reinforcement Learning</h3>
    <div class="authors">Weihua Du⭐️, Jinglun Zhao⭐️, <span class="primary-gradient-text">Chao Yu</span>, Xingcheng Yao, Zimeng Song, Siyang Wu, Ruifeng Luo, Zhiyuan Liu, Xianzhong Zhao, Yi Wu</div>
    <div class="venue">International Joint Conference on Artificial Intelligence (IJCAI 2023)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2306.15182" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2023, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICLR 2023</div>
    <img src='images/learningzeroshot.png' alt="HSP Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Learning Zero-Shot Cooperation with Humans, Assuming Humans Are Biased</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>⭐️, Jiaxuan Gao⭐️, Weilin Liu, Botian Xu, Hao Tang, Jiaqi Yang, Yu Wang, Yi Wu</div>
    <div class="venue">International Conference on Learning Representations (ICLR 2023)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2302.01605" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2023, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">AAMAS 2023</div>
    <img src='images/realtime.png' alt="ACE Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Asynchronous Multi-Agent Reinforcement Learning for Efficient Real-Time Multi-Robot Cooperative Exploration</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>⭐️, Xinyi Yang⭐️, Jiaxuan Gao⭐️, Jiayu Chen, Yunfei Li, Jijia Liu, Yunfei Xiang, Ruixin Huang, Huazhong Yang, Yi Wu, Yu Wang</div>
    <div class="venue">International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2023)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2301.03398" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2023, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">AAMAS 2023</div>
    <img src='images/graphenhan.png' alt="MAGE-X Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Learning Graph-Enhanced Commander-Executor for Multi-Agent Navigation</h3>
    <div class="authors">Xinyi Yang, Shiyu Huang, Yiwen Sun, Yuxiang Yang, <span class="primary-gradient-text">Chao Yu</span>, Wei-Wei Tu, Huazhong Yang, Yu Wang</div>
    <div class="venue">International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2023)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2302.04094" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2022, Journal, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">TCAD 2022</div>
    <img src='images/incame.png' alt="INCAME Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>INCAME: Interruptible CNN Accelerator for Multirobot Exploration</h3>
    <div class="authors">Jincheng Yu, Zhilin Xu, Shulin Zeng, <span class="primary-gradient-text">Chao Yu</span>, Jiantao Qiu, Chaoyang Shen, Yuanfan Xu, Guohao Dai, Yu Wang, Huazhong Yang</div>
    <div class="venue">IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD 2022), 41(4):964-978</div>
      <div class="links"></div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2022, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">NeurIPS 2022</div>
    <img src='images/ppogames.png' alt="MAPPO Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>⭐️, Akash Velu⭐️, Eugene Vinitsky, Jiaxuan Gao, Yu Wang📧, Alexandre Bayen, Yi Wu📧</div>
    <div class="venue">Conference on Neural Information Processing Systems (NeurIPS 2022), Datasets and Benchmarks Track</div>
    <div class="links">
      <a href="https://proceedings.neurips.cc/paper_files/paper/2022/hash/9c1535a02f0ce079433344e14d910597-Abstract-Datasets_and_Benchmarks.html" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://github.com/marlbenchmark/on-policy" class="btn-accent"><i class="fab fa-github"></i> Code</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2022, Conference, CCF-C">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ROBIO 2022</div>
    <img src='images/photo3d.png' alt="Exploration Benchmark Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>A Benchmark of Planning-based Exploration Methods in Photo-Realistic 3D Simulator</h3>
    <div class="authors">Xuan Du⭐️, Xinyi Yang⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️, Jiaxuan Gao, Qingmin Liao, Huazhong Yang, Yu Wang</div>
    <div class="venue">IEEE International Conference on Robotics and Biomimetics (ROBIO 2022)</div>
    <div class="links">
      <a href="http://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/480b3e15-730b-45a9-ae1e-3b447cd28e3b.pdf" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2022, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ECCV 2022</div>
    <img src='images/visual.png' alt="MAANS Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Learning Efficient Multi-Agent Cooperative Visual Exploration</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>⭐️, Xinyi Yang⭐️, Jiaxuan Gao⭐️, Huazhong Yang, Yu Wang, Yi Wu</div>
    <div class="venue">European Conference on Computer Vision (ECCV 2022)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2110.05734" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://sites.google.com/view/maans" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2022, Conference, CCF-C">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICIP 2022</div>
    <img src='images/save.png' alt="SAVE Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>SAVE: Spatial-Attention Visual Exploration</h3>
    <div class="authors">Xinyi Yang⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️, Jiaxuan Gao⭐️, Yu Wang, Huazhong Yang</div>
    <div class="venue">IEEE International Conference on Image Processing (ICIP 2022)</div>
    <div class="links">
      <a href="https://www.researchgate.net/publication/365111412_SAVE_Spatial-Attention_Visual_Exploration" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2022, Conference, CCF-C">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">CoG 2022</div>
    <img src='images/vmapd.png' alt="VMAPD Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>VMAPD: Generate Diverse Solutions for Multi-Agent Games with Recurrent Trajectory Discriminators</h3>
    <div class="authors">Shiyu Huang, <span class="primary-gradient-text">Chao Yu</span>, Bin Wang, Dong Li, Yu Wang, Ting Chen, Jun Zhu</div>
    <div class="venue">IEEE Conference on Games (CoG 2022)</div>
    <div class="links">
      <a href="http://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/7e255313-1442-4481-ad41-ab675770a2b1.pdf" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2022, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICML 2022</div>
    <img src='images/revisiting.png' alt="Revisiting MARL Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Revisiting Some Common Practices in Cooperative Multi-Agent Reinforcement Learning</h3>
    <div class="authors">Wei Fu, <span class="primary-gradient-text">Chao Yu</span>, Zelai Xu, Jiaqi Yang, Yi Wu</div>
    <div class="venue">International Conference on Machine Learning (ICML 2022)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2206.07505" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://sites.google.com/view/revisiting-marl" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2024, Conference, non-CCF">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">CASE 2024</div>
    <img src='images/vulner.png' alt="Hazard Arbitration Reward Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Multi-Agent Vulnerability Discovery for Autonomous Driving Policy by Finding AV-Responsible Scenarios</h3>
    <div class="authors">Ye Mu⭐️, Weilin Liu⭐️, <span class="primary-gradient-text">Chao Yu</span>, Xuefei Ning📧, Zhong Cao, Zelai Xu, Yi Wu, Shuang Liang, Qingmin Liao, Huazhong Yang, Yu Wang📧</div>
    <div class="venue">IEEE International Conference on Automation Science and Engineering (CASE 2024)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2112.06185" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2021, Conference, CCF-C">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">CICAI 2021</div>
    <img src='images/mappo.png' alt="async-MAPPO Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Unlocking the Potential of MAPPO with Asynchronous Optimization</h3>
    <div class="authors">Wei Fu, <span class="primary-gradient-text">Chao Yu</span>, Yunfei Li, Yi Wu</div>
    <div class="venue">CAAI International Conference on Artificial Intelligence (CICAI 2021)</div>
    <div class="links">
      <a href="https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/698728b2-2b03-4ec2-98be-d675dbb2779b.pdf" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2021, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICLR 2021</div>
    <img src='images/Reward-Randomization.png' alt="Reward Randomization Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Discovering Diverse Multi-agent Strategic Behavior Via Reward Randomization</h3>
    <div class="authors">Zhenggang Tang⭐️, <span class="primary-gradient-text">Chao Yu</span>⭐️, Boyuan Chen, Huazhe Xu, Xiaolong Wang, Fei Fang, Simon Du, Yu Wang, Yi Wu</div>
    <div class="venue">International Conference on Learning Representations (ICLR 2021)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/2103.04564" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
      <a href="https://sites.google.com/view/staghuntrpg" class="btn-accent"><i class="fas fa-globe"></i> Project</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2020, Conference, CCF-A">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">NeurIPS 2020 Workshop</div>
    <img src='images/Benchmarking-Multi-agent.png' alt="Benchmarking Multi-agent Deep Reinforcement Learning Algorithms Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Benchmarking Multi-agent Deep Reinforcement Learning Algorithms</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>⭐️, Akash Velu⭐️, Eugene Vinitsky, Yu Wang, Alexandre Bayen, Yi Wu</div>
    <div class="venue">Conference on Neural Information Processing Systems (NeurIPS 2020), Workshop</div>
      <div class="links"></div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2020, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">DAC 2020</div>
    <img src='images/inca.png' alt="INCA Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>INCA: INterruptible CNN Accelerator for Multi-tasking in Embedded Robots</h3>
    <div class="authors">Jincheng Yu, Zhilin Xu, Shulin Zeng, <span class="primary-gradient-text">Chao Yu</span>, Jiantao Qiu, Chaoyang Shen, Yuanfan Xu, Guohao Dai, Yu Wang, Huazhong Yang</div>
    <div class="venue">ACM/IEEE Design Automation Conference (DAC 2020)</div>
    <div class="links">
      <a href="https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/publications/2020/DAC20_299_2gfq3TE.pdf" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2020, Conference, CCF-C">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">RAW 2020</div>
    <img src='images/cnnfpga.png' alt="Monocular DSLAM Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>CNN-based Monocular Decentralized SLAM on embedded FPGA</h3>
    <div class="authors">Jincheng Yu, Feng Gao, Jianfei Cao, <span class="primary-gradient-text">Chao Yu</span>, Zhaoliang Zhang, Zhengfeng Huang, Yu Wang, Huazhong Yang</div>
    <div class="venue">IEEE Reconfigurable Architectures Workshop (RAW 2020)</div>
    <div class="links">
      <a href="https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/publications/2020/RAW20_308.pdf" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2020, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">FCCM 2020</div>
    <img src='images/cnnfpga2.png' alt="Feature-point Extraction Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>CNN-based Feature-point Extraction for Real-time Visual SLAM on Embedded FPGA</h3>
    <div class="authors">Zhilin Xu, Jincheng Yu, <span class="primary-gradient-text">Chao Yu</span>, Hao Shen, Yu Wang, Huazhong Yang</div>
    <div class="venue">IEEE Symposium on Field-Programmable Custom Computing Machines (FCCM 2020)</div>
    <div class="links">
      <a href="https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/publications/2020/FCCM20_303.pdf" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2019, Conference, CCF-C">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ICCRT 2019</div>
    <img src='images/longsight.png' alt="Long-Sighted IL Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Long-Sighted Imitation Learning for Partially Observable Control</h3>
    <div class="authors">Bo Xiong, Fangshi Wang, <span class="primary-gradient-text">Chao Yu</span>, Fei Qiao, Xin-Jun Liu</div>
    <div class="venue">International Conference on Control and Robot Technology (ICCRT 2019)</div>
    <div class="links">
      <a href="https://dl.acm.org/doi/10.1145/3387304.3387320" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2019, Conference, CCF-C">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ROBIO 2019</div>
    <img src='images/densenet.png' alt="DenseNet Loop Closure Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>A DenseNet feature-based loop closure method for visual SLAM system</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>, ZuXin Liu, Xin-Jun Liu, Fei Qiao, Yu Wang, Fugui Xie, Qi Wei, Yi Yang</div>
    <div class="venue">IEEE International Conference on Robotics and Biomimetics (ROBIO 2019)</div>
    <div class="links">
      <a href="https://doi.org/10.1109/ROBIO49542.2019.8961714" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2018, Conference, CCF-B">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">IROS 2018</div>
    <img src='images/dsslam.png' alt="DS-SLAM Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>DS-SLAM: A Semantic Visual SLAM towards Dynamic Environments</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>, Zuxin Liu, Xin-Jun Liu, Fugui Xie, Qiao Fei</div>
    <div class="venue">IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2018)</div>
    <div class="links">
      <a href="https://arxiv.org/abs/1809.08379" class="btn-accent"><i class="fas fa-file-alt"></i> Paper</a>
    </div>
  </div>
</div>

<div class='paper-box floating-card' data-tags="2017, Conference, CCF-C">
  <div class='paper-box-image'>
    <div class="badge pulse-accent">ROBIO 2017</div>
    <img src='images/Multi-robot-Coordination.png' alt="Multi-robot Coordination Overview" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Multi-robot coordination for high-speed pick-and-place tasks</h3>
    <div class="authors"><span class="primary-gradient-text">Chao Yu</span>, Xin-Jun Liu, Fei Qiao, Fugui Xie</div>
    <div class="venue">IEEE International Conference on Robotics and Biomimetics (ROBIO 2017)</div>
    <div class="links"></div>
  </div>
</div>

</div>

<span class='anchor' id='-awards'></span>
# 🏆 Awards
- *2024*: &nbsp;China Postdoctoral Excellent Special <span class="primary-gradient-text">Foundation</span> (Top 1,000 nationwide), Chinese Postdoctoral Science Foundation (CPSF).
- *2024*: &nbsp;Postdoctoral <span class="primary-gradient-text">Fellowship</span> Program (Top 3,000 nationwide), Chinese Postdoctoral Science Foundation (CPSF).
- *2024*: &nbsp;Runner-up for Outstanding Doctoral <span class="primary-gradient-text">Thesis</span> (Top 5), Chinese Intelligent Agent and Multi-Agent Systems.
- *2023*: &nbsp;Shuimu <span class="primary-gradient-text">Scholar</span> Program, Tsinghua University.
- *2023*: &nbsp;Chuanxin Future <span class="primary-gradient-text">Scholar</span> Program, Department of Electronic Engineering, Tsinghua University.
- *2023*: &nbsp;Zhang Keqian Postdoctoral <span class="primary-gradient-text">Fellowship</span>, Department of Electronic Engineering, Tsinghua University.
- *2023*: &nbsp;Outstanding Doctoral <span class="primary-gradient-text">Thesis</span> (Top 10%), Tsinghua University.
- *2023*: &nbsp;Outstanding Doctoral <span class="primary-gradient-text">Graduate</span> (Top 5%), Tsinghua University.
- *2019*: &nbsp;Outstanding Master's <span class="primary-gradient-text">Thesis</span> (Top 10%), Tsinghua University.
- *2019 - 2023*: &nbsp;First-Class <span class="primary-gradient-text">Scholarship</span> (3 times), Tsinghua University.
- *2015*: &nbsp;National <span class="primary-gradient-text">Scholarship</span>, China Ministry of Education.

<span class='anchor' id='-talks'></span>
# 🎤 Talks
- *2026.08.05*: &nbsp;[**智源专访：具身智能下一步，走向“模型 + 系统”协同**](https://mp.weixin.qq.com/s/KSXKy7nVAQ8eshrBRtGnUA)
- *2026.07.19*: &nbsp;[**WAIC国地中心报告**](https://mp.weixin.qq.com/s/h2LFwznlp_NDzTl7kPscTA)
- *2026.07.12 - 2026.07.18*: &nbsp;[**RSS workshop**](https://mp.weixin.qq.com/s/YfC_vc-I6xebAR1_tlZa4Q)
- *2026.06.13*: &nbsp;[**智源大会报告**](https://mp.weixin.qq.com/s/IR7QBVaLNWNhFK6XY6ZUNA)
- *2026.06.05*: &nbsp;[**华为云技术报告**](https://mp.weixin.qq.com/s/ibGUxZF3bIe_XkZ5v4bivw)
- *2026.05.23*: &nbsp;[**杭州蚂蚁开源报告**](https://mp.weixin.qq.com/s/FDudzltGtjE9kaJDKkVx0w)
- *2026.01.15*: &nbsp;[**北京人形机器人创新中心报告**](https://mp.weixin.qq.com/s/EAoC-iDPpBPAwRnzlR126w)

<span class='anchor' id='-live'></span>
# 📺 Live
- *2026.08.08*: &nbsp;张翼显（青稞）— [**从端到端 VLA 到 Harness VLA：面向具身智能与机器人操作任务的记忆增强式执行框架**](qingkeai.online)
- *2026.07.29*: &nbsp;张翼显（XRobotics）— [**Harness VLA：可持续进化的具身智能体系统**](https://weixin.qq.com/sph/ASMB0IqMPD)
- *2026.04.22*: &nbsp;徐哲轩、苑会宁、徐泽来（将门）— [**大模型在多智能体任务中的评估、训练与Scaling**](https://mp.weixin.qq.com/s/G-o5TURksIgVZGRsbDfqJw)
- *2026.04.14*: &nbsp;苑会宁、张翼显（智源大厦 ICLR 分享）— [**ICLR 预讲会**](https://mp.weixin.qq.com/s/AzyUvWU6HKq7cJWOXkLUdg)
- *2026.04.10*: &nbsp;施良致（3D视觉工坊）— [**只用20条真实数据训练机器人？RL-Co：强化学习驱动的仿真-真机协同训练**](https://mp.weixin.qq.com/s/g6p_Fl8dGk9qy1AksQiABg)
- *2026.03.24*: &nbsp;徐哲轩（青稞）— [**从 Depth Scaling 到 Width Scaling！WideSeek-R1：通过多智能体 RL 探索大模型的广度扩展**](https://www.bilibili.com/video/BV1bgQSBnEs6/)
- *2026.03.10*: &nbsp;臧宏之（青稞）— [**一起聊聊RLinf-USER：面向现实世界机器人在线策略学习的统一且可扩展系统**](https://mp.weixin.qq.com/s/2FjaoeuHsPEnAhVUPLOtVw)
- *2026.03.08*: &nbsp;于舒昂（Xbotics）— [**RLinf-USER：真实世界在线进化，从系统瓶颈到统一高效，让具身智能真正“活起来”**](https://mp.weixin.qq.com/s/9VoCpyjsoqQL_7bCATKaEg)
- *2025.12.28*: &nbsp;于超（青稞 AI 嘉年华）— [**具身智能专题｜2025 “青稞” AI 嘉年华**](https://www.bilibili.com/video/BV1tDqwB2EZ5/)
- *2025.12.25*: &nbsp;韦明杰（计算机视觉life）— [**RLinf-VLA框架技术报告——RL如何训练VLA？**](https://www.bilibili.com/video/BV1dxBoBLEWf/)
- *2025.12.15*: &nbsp;张瑞泽、季世龙（深蓝）— [**NeurIPS'25 & CoRL'25｜无人机也能打排球吗？来看看清华团队的解决方案**](https://mp.weixin.qq.com/s/HvLJCr_PNsY0fsx1vS4CXQ)
- *2025.12.09*: &nbsp;陈康（深蓝）— [**对话πRL一作：RLinf流匹配 VLA 在线强化学习框架！π系列模型成功率提升至98%**](https://mp.weixin.qq.com/s/UNpmZgqLHOSdKnhMWr1ybg)
- *2025.12.06*: &nbsp;陈康（青稞）— [**从 π\_0 到 π\_RL：面向流匹配 VLA 的强化学习后训练框架**](https://www.bilibili.com/video/BV1Tt2sBPEix/)
- *2025.12.02*: &nbsp;臧宏之（青稞）— [**RLinf-VLA 实践：从零上手 VLA（OpenVLA）强化学习**](https://www.bilibili.com/video/BV1CF24BcEwb/)
- *2025.12.02*: &nbsp;徐泽来（将门创投）— [**大模型智能体可以玩好狼人杀吗？**](https://www.techbeat.net/talk-info?id=1012)
- *2025.11.27*: &nbsp;刘志豪（3D视觉工坊）— [**清华开源｜πRL：首个面向流匹配 VLA 的在线强化学习微调框架**](https://www.bilibili.com/video/BV11dSgBbEWp/)
- *2025.11.26*: &nbsp;张同和、高枫（将门创投）— [**清华RLinf团队: RL可以为VLA带来什么？**](https://mp.weixin.qq.com/s/MxxzzzGSk2xORpJqCvgOkQ)
- *2025.11.25*: &nbsp;林灏（青稞）— [**一起聊聊具身智能 RL 训练框架 RLinf 的系统设计**](https://mp.weixin.qq.com/s/3xR_cHk1Lqx-uUjUNw99_Q)
- *2025.11.12*: &nbsp;韦明杰（3D视觉工坊）— [**统一高效 VLA+RL 训练框架：RLinf-VLA——RL 如何训练 VLA？**](https://www.bilibili.com/video/BV1RjC7B2E1S/)
- *2025.11.10*: &nbsp;陈康（具身智能之心）— [**πRL：首个面向流匹配 VLA 的强化学习微调框架**](https://www.bilibili.com/video/BV1Hd2HB7EUy/)
- *2025.10.31*: &nbsp;徐泽来、于超（B站）— [**2025 bilibili超级科学晚全程回顾**](https://b23.tv/nUEJHVU)
- *2025.10.28*: &nbsp;高枫、臧宏之（具身智能之心）— [**SFT 还是RL，VLA到底应该如何训练？**](https://mp.weixin.qq.com/s/DMSuxBon8c9CNaAjU1vZZw)
- *2025.07.18*: &nbsp;高枫（MSRA）— [**待补充标题**](待补充链接)

<span class='anchor' id='-services'></span>
# 👓 Projects
- *Projects*: &nbsp;[1] 基于深度强化学习的多无人机追逃博弈决策和控制关键技术研究，国家自然科学基金委，青年科学基金项目（C类）, 2025-2027.
- *Projects*: &nbsp;[2] 多机协同高效机器学习系统研究，国家自然科学基金-中德合作交流基金, 2021-2025.
- *Projects*: &nbsp;[3] 具有强推理能力的大语言模型智能体关键技术研究，中国博士后基金特别资助, 2023-2025.

<span class='anchor' id='-internships'></span>
# 💼 Work Experience
- *2026.01 - Present*: &nbsp;Assistant Professor, Tsinghua University.
- *2023.07 - 2025.12*: &nbsp;Postdoctoral Researcher, Tsinghua University.

<span class='anchor' id='-recruitment'></span>
# 🙋 Recruitment

<style>
.recruit-card {
  margin: 2rem 0;
  padding: 2.2rem 2rem 2rem 2rem;
  background: #f5f2ee;
  border: 2px solid #d8d0c7;
  border-top: 6px solid #c69c6d;
  border-radius: 1.8rem;
  box-shadow: 0 1px 0 rgba(0,0,0,0.03) inset;
}

.recruit-title {
  margin: 0 0 1.4rem 0;
  font-size: 2.6rem;
  font-weight: 800;
  line-height: 1.2;
  color: #8b572a;
  font-family: Georgia, "Times New Roman", serif;
}

.recruit-text {
  margin: 0 0 1.6rem 0;
  font-size: 1.25rem;
  line-height: 1.75;
  color: #203047;
  font-weight: 650;
}

.recruit-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
  margin: 1.2rem 0 1.8rem 0;
}

.recruit-tag {
  display: inline-block;
  padding: 1rem 1.8rem;
  background: #ffffff;
  border: 2px solid #d8d3cd;
  border-radius: 1rem;
  color: #14263d;
  font-size: 1.05rem;
  font-weight: 800;
  line-height: 1.4;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}

.recruit-divider {
  height: 1px;
  background: #e6e1da;
  margin: 1.8rem 0 1.8rem 0;
}

.recruit-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 1.4rem;
}

.recruit-btn {
  display: inline-block;
  padding: 1rem 2rem;
  min-width: 240px;
  text-align: center;
  text-decoration: none !important;
  color: #ffffff !important;
  font-size: 1.05rem;
  font-weight: 800;
  border-radius: 1rem;
  background: linear-gradient(180deg, #2c6aa0 0%, #1f5c91 100%);
  box-shadow: 0 8px 18px rgba(30, 75, 120, 0.18);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.recruit-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 22px rgba(30, 75, 120, 0.22);
}

@media (max-width: 768px) {
  .recruit-card {
    padding: 1.5rem 1.2rem;
    border-radius: 1.2rem;
  }

  .recruit-title {
    font-size: 2rem;
  }

  .recruit-text {
    font-size: 1.05rem;
    line-height: 1.65;
  }

  .recruit-tag {
    width: 100%;
    box-sizing: border-box;
  }

  .recruit-btn {
    width: 100%;
    min-width: unset;
  }
}
</style>

<div class="recruit-card">
  <h2 class="recruit-title">We are actively recruiting!</h2>

  <p class="recruit-text">
    We are looking for Ph.D. and Master students, Postdocs at Tsinghua University, Ph.D. students of the Joint Program of Zhongguancun Academy and Tsinghua University and Undergraduate Interns
    with strong interests and motivation to work on frontier research topics including:
  </p>

  <div class="recruit-tags">
    <div class="recruit-tag">Reinforcement learning &amp; embodied intelligence infrastructure</div>
    <div class="recruit-tag">Embodied agent &amp; embodied large model training</div>
    <div class="recruit-tag">Strategic agent</div>
    <div class="recruit-tag">Open source community</div>
  </div>

  <p class="recruit-text" style="margin-bottom:0;">
    Candidates with hands-on systems building abilities and mathematical background are highly encouraged.
  </p>

  <div class="recruit-divider"></div>

  <div class="recruit-buttons">
    <a class="recruit-btn" href="https://thusigs-edi-lab.github.io/contact/">Application →</a>
    <a class="recruit-btn" href="https://nics-efc.feishu.cn/wiki/I6RSw44u0iOibhkviXjcAVZRn5Q?from=from_copylink">RLinf related work →</a>
  </div>
</div>

<span class='anchor' id='-bond'></span>
# 🔗 Bond
<div class='paper-box floating-card'>
  <div class='paper-box-image'>
    <div class="badge pulse-accent">EE, THU</div>
    <img src='images/nicslogo.png' alt="nicslogo" width="100%">
  </div>
  <div class='paper-box-text'>
    <h3>Energy Efficient Computing Group</h3>
    <div class="venue">Nanoscale Integrated Circuits and System Lab, Energy Efficient Computing Group (NICS-EFC)  is leaded by Professor Yu Wang, in Electronic Engineering  Department, Tsinghua University. The group is committed to the research of energy-efficient circuits and systems design methodology towards the Artificial Intelligence (AI) scenario: Multi-agent Reinforcement Learning Algorithm, Efficient and Robust DL system, Domain Specific Acceleration, and Multi-agent system. Each direction is headed by a research associate. </div>
    <div class="links">
      <a href="https://nicsefc.ee.tsinghua.edu.cn/" class="btn-accent"><i class="fas fa-file-alt"></i> Link</a>
    </div>
  </div>
</div>

<!-- <div style="text-align: center;"> -->
<div style="width: 20%; position:relative; left:40%">
  <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=Vr-eYn9fNnJRWR6kcXJa5akQlOll4HKWjM--Xfn5inY"></script>
    <!-- 地图小部件代码结束 -->
</div>


<script>
document.addEventListener('DOMContentLoaded', function() {
  const wrapper = document.getElementById('publications-wrapper');
  if (!wrapper) return;

  const filterContainer = document.getElementById('filter-container');
  const paperBoxes = wrapper.querySelectorAll('.paper-box');
  
  let tagCounts = {}; 
  let activeTags = new Set();

  // 初始化：生成标签并统计数量
  paperBoxes.forEach(box => {
    const tagsAttribute = box.getAttribute('data-tags');
    if (tagsAttribute) {
      const tagsList = tagsAttribute.split(',').map(t => t.trim()).filter(t => t);
      
      // --- 插入标签到 Links 上方 ---
      const textContainer = box.querySelector('.paper-box-text');
      const linksContainer = box.querySelector('.links');
      
      if (textContainer && !textContainer.querySelector('.badge-container')) {
        const badgeContainer = document.createElement('div');
        badgeContainer.className = 'badge-container';
        
        tagsList.forEach(tag => {
          const badge = document.createElement('span');
          badge.className = 'inner-tag-badge';
          badge.textContent = tag;
          badgeContainer.appendChild(badge);
        });
        
        if (linksContainer) {
          textContainer.insertBefore(badgeContainer, linksContainer);
        } else {
          textContainer.appendChild(badgeContainer);
        }
      }
      // ---------------------------

      tagsList.forEach(tag => {
        tagCounts[tag] = (tagCounts[tag] || 0) + 1;
      });
    }
  });

  // 生成顶部过滤按钮
  const sortedTags = Object.keys(tagCounts).sort();
  if (filterContainer) {
    filterContainer.innerHTML = ''; 
    sortedTags.forEach(tag => {
      const btn = document.createElement('button');
      btn.className = 'filter-btn';
      btn.textContent = `${tag} (${tagCounts[tag]})`;
      
      btn.onclick = () => {
        if (activeTags.has(tag)) {
          activeTags.delete(tag);
          btn.classList.remove('active');
        } else {
          activeTags.add(tag);
          btn.classList.add('active');
        }
        filterPapers(); // 点击后触发过滤和高亮更新
      };
      
      filterContainer.appendChild(btn);
    });
  }

  // 🔥 核心逻辑更新：过滤论文 + 高亮标签
  function filterPapers() {
    paperBoxes.forEach(box => {
      // 1. 处理卡片显示/隐藏
      const boxTagsString = box.getAttribute('data-tags');
      const boxTags = boxTagsString ? boxTagsString.split(',').map(t => t.trim()) : [];
      
      let isVisible = true;
      if (activeTags.size > 0) {
        if (boxTags.length === 0) {
          isVisible = false;
        } else {
          // 必须包含所有选中的标签 (AND 逻辑)
          isVisible = Array.from(activeTags).every(activeTag => boxTags.includes(activeTag));
        }
      }

      if (isVisible) {
        box.classList.remove('hidden');
      } else {
        box.classList.add('hidden');
      }

      // 2. 🔥 处理内部标签的高亮 (即便卡片隐藏了，逻辑上也更新一下，没坏处)
      const innerBadges = box.querySelectorAll('.inner-tag-badge');
      innerBadges.forEach(badge => {
        // 如果这个小标签的文字，存在于 activeTags (顶部选中的集合) 中，就变色
        if (activeTags.has(badge.textContent)) {
          badge.classList.add('active');
        } else {
          badge.classList.remove('active');
        }
      });
    });
  }
});
</script>

# 2024-DSP-Experiment
数字信号处理实验2-实验一二代码

## 硬件要求
支持M系列芯片的Mac平台上的mps加速、支持CUDA的NVIDIA显卡。
建议拥有一张NVIDIA RTX 3060以上的显卡，显存至少6GB。

## QuickSetup
### 1. 安装CUDA及cuDNN（可选）
1. 安装CUDA
   - 下载地址：https://developer.nvidia.com/cuda-downloads
   - 安装教程：https://docs.nvidia.com/cuda/cuda-installation-guide-mac-os-x/index.html

2. 安装cuDNN
    - 下载地址：https://developer.nvidia.com/cudnn
    - 安装教程：https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html

根据以上教程自行安装CUDA加速库和cuDNN深度学习库。

### 2. 配置Python环境
Python版本应在3.8及以上，目前在3.10.6上测试成功。推荐使用Anaconda进行环境管理。
运行以下命令安装依赖：
```shell
pip install -r requirements.txt
```

将FFmpeg.exe和FFprobe.exe放置在当前工作目录下。

### 3. 启动项目
1. 可以选择官方默认的WebUI界面，点击`go-webui.bat`即可启动。
    - 详见白菜工厂的文档：https://www.yuque.com/baicaigongchang1145haoyuangong/ib3g1e

2. 点击AudioKit-DSPedit.exe即可启动本次实验的GUI界面。
## 游戏配音识别项目

### 项目的文件结构

```
project
|	Preprosse.py
|   Mydataset.py
|	Model.py
|	Create_Hparams.py
|	Trainer.py
|	loss_look.py
|	main.py
└---data
|	| 
|	└---0
|	|	| 0(1).wav
|	|	| ....
|	└---1
|	|	| 1(1).wav
|	|	| ....
|	└---2
|	|	| 2(1).wav
|	|	| ....
|	└---3
|	|	| 3(1).wav
|	|	| ....
|
└---Experiments
|	| v0
|	| v1
|	| ....
|
└---np_data
|	|
|	└--- 0
|	|	 | 0(1).npy
|	|	 | ...
|	└--- 1
|	|	 | 1(1).npy
|	|	 | ...
|	└--- 2
|	|	 | 2(1).npy
|	|	 | ...
|	└--- 3
|	|	 | 3(1).npy
|	|	 | ...
```

- Preprocess.py ：将语音的转成梅尔谱，利用`np.save`保存成`numpy`形式的据怎，保存到np_data的文件夹中

- Model.py : 神经网络模型文件
- Mydataset.py ：dataset类编写文件（利用np_data中的数据集进行完成的编写）
- Create_Hparams.py ：训练时参数类（超参数、实验结果保存路径、数据集路径等）
- Trainer.py ：训练器
- main.py ： 主程序入口
- loss_look.py ：实验结束后，查看loss和acc走势的脚本

### 项目简介

​	本项目是对于游戏的配音进行识别的一个项目（针对于lol中的每个角色的配音），主要是对于不同人物的配音可能是同一个人，但是他们的声音有很不同，本项目就是像验证对于这样的特点很明显的同一个人配的音可不可以用深度学习的方法识别出来。

​	本实验的数据集来自lol游戏中的内置语音包，我们没有提取全部的数据，大约所有的数据一共1.5G左右包含4个配音员的配音。

​	本实验的语音提取的形式是，*.wav提取到梅尔谱，利用`numpy`进行保存提取后的数据；

### 项目依赖

- `pytorch` 
- `torchaudio:一般来说pytorch自带这个包`
- `liborsa`
- `pathlib`
- `sklearn`

### 项目运行

- 首先，你需要得到np_data的 `*.npy` 的数字化文件数据，利用Preprosse.py中的`extract_mel_feature_bytaco`函数进行提取np_data，同时得到帧长的一个分布图
- 在完成上一步的后，运行`main.py`主函数入口，进行训练（注意修改参数`ver`,表示每次不同训练代表的不同的版本）
- 完成后，可以利用`loss_look.py`脚本观察训练时的衡量训练过程中的参数变化
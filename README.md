# 分类：用声呐发现未爆炸的水雷
## 小项目介绍
数据来源于实验：测试声呐是否可以用于检测在港口军事行动后遗留下来的未爆炸的水雷，声呐信号在一个脉冲期间频率会增加或降低。该数据集的测试值代表声呐接收器在不同地点接收到的返回信号，一半声呐信号反映的是岩石形状，而另一半是水雷的形状。
## 数据集分析
     read_data.py : 读取数据到列表，确定数据集规模。
       corrCalc.py: 皮尔逊相关系数
       corrPlot.py: 属性交会图
  data_analysis.py: 统计数据
    data_counts.py: 确定属性特征
      linePlots.py: 利用平行坐标图可视化数据
 pandasReadSummarize.py: 利用pandas读取数据，将数据读入dataframe，并且查看基本统计信息。
       plotAttribute.py: 利用分位数图查看数据异常点
   sampleCorrHeatMap.py: 热力图
          targetCorr.py: 属性、标签相关性
## 运行环境
python3.7
## 总结
相比纯利用python，可以选择调用python数据处理库，而且利用jupyter notebook会更方便。

# Deepracer-CommunityRaces
此競賽由InnoServer所舉辦，在AWS Deepracer創建社區競賽，分為初賽及決賽，初賽選取前20名晉級，最終以決賽第三名獲得佳績。  

<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/InnoServe-Super-Pui-Pui-Car-2.jpg"  width = "575"/>

# 初賽
所選賽道: Competition track  
競賽規則: 連續3圈/界外懲罰3秒/計時賽  
  
<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/002.png" width = "575"/>  

# 訓練過程
初始訓練先從選擇動作方面我以離散動作為主，雖然在數量有限的動作中不一定能走到路徑最佳解，不過在訓練神經網路方面，比起連續動作更能獲得較快的收斂結果。  
動作選擇與參數調整如下圖:  
  
<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/test1-3.png" width = "775"/>  
  
一共13組動作因子，並根據轉向角度調整速率高低，並且除了轉向角度0°的動作外，每組轉向角度都會配置基於速率1.8 m/s區隔，更快或更慢的調配速率，讓Deeprace 
  
# 決賽
所選賽道: Competition track  
競賽規則: 連續4圈/界外懲罰5秒/計時賽。

（更新中...）
  

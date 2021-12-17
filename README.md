# Deepracer-CommunityRaces
此競賽由InnoServer所舉辦，在AWS Deepracer創建社區競賽，分為初賽及決賽，初賽選取前20名晉級，最終以決賽第三名獲得佳績。  

<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/InnoServe-Super-Pui-Pui-Car-2.jpg"  width = "575"/>

# 初賽
所選賽道: Competition track  
競賽規則: 連續3圈/界外懲罰3秒/計時賽  
  
<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/002.png" width = "575"/>  

# 訓練過程
初始訓練先從選擇動作方面我以離散動作為主，雖然在數量有限的動作中不一定能走到路徑最佳解，不過在訓練神經網路方面，比起連續動作更能獲得較快的收斂結果。 我們一共設置13組動作因子，並根據轉向角度調整速率高低，並且除了轉向角度0°的動作外，每組轉向角度都會配置基於基準速率1.8 m/s區隔，更快或更慢的調配速率，讓Deeprace 能有更佳的動作選擇。在獎勵程式碼中，我們引用來自悉尼大學MatthewSuntup所提供的`def identify_corner()` 角度判別、`def select_speed()` 速度選擇，透過判斷未來步數中的航路點角度是否超過閥值，進而判斷是否選用基於速率1.8 m/s的速度進行加速。  
  
學習初期，需要將學習率調大(0.001~0.0009)、選取較少量梯度下降的batch size (32-64) 促使前期訓練速度加快，達到有效率的訓練。
  
<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/test1-3.png" width = "675"/>  
<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/reward1-3.png" width = "375"/>  

  
# 決賽
所選賽道: Competition track  
競賽規則: 連續4圈/界外懲罰5秒/計時賽。
  
<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/003.png" width = "575"/>  

# 訓練過程
透過觀察log日誌發現有些動作再選用上機率特別小，並且整體速度無法達成理想，因此後續不斷嘗試更新動作的速度值，並且些微提高即改良，在角度判斷上也將基準速率 1.8 m/s 提升至 2.0 m/s ，經過多次的訓練，將降低學習率、增加梯度下降的batch size和迭代次數來達到收斂。並且需要確保賽車能完整跑完軌道，因為出借懲罰5秒對於比賽結果傷害極大。

<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/test1-15-1.jpg" width = "675"/>  
<img src = "https://github.com/ZaWaLuDo77/Deepracer-CommunityRaces/blob/main/picture/reward1-15-1.png" width = "375"/>  

# 參考資料
MatthewSuntup/DeepRacer: https://github.com/MatthewSuntup/DeepRacer#About  
An Advanced Guide to AWS DeepRacer: https://towardsdatascience.com/an-advanced-guide-to-aws-deepracer-2b462c37eea

  

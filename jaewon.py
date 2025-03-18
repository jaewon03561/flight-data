import pandas as pd
import numpy as np
from nycflights13 import flights, planes
import pandas as pd
air_line= pd.merge(flights,planes, on = "tailnum", how= "left")
air_line.head()



##### 계절별 출발 딜레이 시간 상관관계 분석 ######

import numpy as np
import pandas as pd

# 계절 컬럼 추가
conditions = [
    (air_line["month"].isin([12, 1, 2])),  # 겨울
    (air_line["month"].isin([3, 4, 5])),   # 봄
    (air_line["month"].isin([6, 7, 8])),   # 여름
    (air_line["month"].isin([9, 10, 11]))  # 가을
]

season_labels = ["Winter", "Spring", "Summer", "Autumn"]

air_line["season"] = np.select(conditions, season_labels, default="Unknown")


season_delay = air_line.groupby("season")["dep_delay"].mean().reset_index()


import seaborn as sns
import matplotlib.pyplot as plt

# 시각화
plt.figure(figsize=(8, 6))
sns.barplot(data=season_delay, x="season", y="dep_delay", palette="coolwarm")

# 제목 및 레이블 설정
plt.title("Average Flight Delay by Season")
plt.xlabel("Season")
plt.ylabel("Average Departure Delay (minutes)")
plt.show()

###################################################



## 데이터 1
### 계절과 딜레이 시간이 관계가 있을 것이다. ###
### 시즌이라는 데이터를 만들어서 한번 해보자 ###

import matplotlib.pyplot as plt
import seaborn as sns

dep_delay_avg = air_line.groupby("month")["dep_delay"].mean()
plt.bar(dep_delay_avg.index, dep_delay_avg)
plt.ylabel('delay')
plt.xlabel("month") 
plt.show()

arr_delay_avg = air_line.groupby("month")["arr_delay"].mean(numeric_only= True)
plt.scatter(arr_delay_avg.index, arr_delay_avg)
plt.ylabel('delay')
plt.xlabel("month") 
plt.show()

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], "ro")


import numpy as np
data = {
    "x" : np.arange(50),
    "y" : np.random.randn(50) * 10
}

plt.scatter('x', 'y', data = data)


## 좌석수와 출발, 도착시간 딜레이간의 딜레이가 있을것이다. 
air_line["carrier"].unique()

corr_mat = air_line[["seats", "dep_delay", "arr_delay"]].corr()

plt.figure(figsize= (6,5))
sns.heatmap(corr_mat,
            annot = True, cmap = "coolwarm",
            fmt = ".2f", linewidths = 0.5)
plt.show()

# 0.91 출발시간의 딜레이와 도착시간의 딜레이가 연관있을 듯
plt.figure(figsize=(6,5))
sns.scatterplot(data= air_line,
                x = "arr_delay", y = "dep_delay")
plt.xlabel("arr_delay")
plt.ylabel("dep_delay")
plt.show


## 엔진개수에 따른 비행거리의 상관관계 ##
import matplotlib.pyplot as plt
import seaborn as sns


import matplotlib.pyplot as plt
import seaborn as sns


### 산점도로 가보자 ###
plt.figure((8,5))
sns.scatterplot(data=air_line, x= "engines", y = "distance", alpha = 0.5)
plt.xlabel("Number of Engines")  # x축 라벨
plt.ylabel("Flight Distance") 
plt.show()

### 막대 차트로 ###
engine_distance = air_line.groupby("engines")["distance"].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(data = engine_distance, x = "engines", y = "distance", palette= "Pastel1")
plt.show()




### 여름에 이용객이 많은건지
## 단지 여름이어서 그런건지

air_line.columns


## 가설 1 여름의 경우 비행기의 좌석 수(이용객이)가 더 많을 것인가?
summer_seat = air_line.loc[air_line["season"] == "Summer","seats"].mean()
winter_seat = air_line.loc[air_line["season"] == "Winter","seats"].mean()
spring_seat = air_line.loc[air_line["season"] == "Spring","seats"].mean()
autumn_seat = air_line.loc[air_line["season"] == "Autumn","seats"].mean()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 계절별 평균 좌석 수 데이터프레임 생성
seat_avg_df = pd.DataFrame({
    "season": ["Summer", "Winter", "Spring", "Autumn"],
    "seats": [summer_seat, winter_seat, spring_seat, autumn_seat]
})

# 바 차트 그리기
plt.figure(figsize=(8,5))
sns.barplot(data=seat_avg_df, x="season", y="seats", palette="coolwarm")  # y="seats"로 수정
plt.title("Average Number of Seats by Season")
plt.xlabel("Season")
plt.ylabel("Average Seats")
plt.show()


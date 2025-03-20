from nycflights13 import flights, planes, weather
import pandas as pd
flights_weather = pd.merge(flights, weather, on = ["year", "month", "day", "hour", "origin"], how = "inner")

flights_weather["origin"]





## 비행기 운항 시, 지연에 영향을 미치는 요소를 살펴보기
# 풍속이 높을 수록, 비행기 딜레이 지연시간이 높을듯.


## 공항별 풍속이 많을 수록 딜레이 시간이 적을 것이다. ##


import matplotlib.pyplot as plt
import seaborn as sns

# 공항별 평균 풍속과 딜레이 정렬
windspeed_avg = flights_weather.groupby("origin")["wind_speed"].mean().sort_values()
arr_delay_origin = flights_weather.groupby("origin")["arr_delay"].mean().reindex(windspeed_avg.index)

fig, ax1 = plt.subplots(figsize=(8,5))

# 막대 그래프로 풍속 시각화 (왼쪽 y축)
ax1.bar(windspeed_avg.index, windspeed_avg, color='skyblue', alpha=0.7, label="Avg Wind Speed")
ax1.set_ylabel("Average Wind Speed (mph)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 선 그래프로 지연 시간 시각화 (오른쪽 y축)
ax2 = ax1.twinx()
ax2.plot(arr_delay_origin.index, arr_delay_origin, 'ro-', label="Avg arrive Delay")
ax2.set_ylabel("Average Departure Delay (min)", color='red')
ax2.tick_params(axis='y', labelcolor='red')

# 제목 및 레이아웃 조정
plt.title("Average Wind Speed vs Departure Delay by Airport")
ax1.set_xlabel("Airport")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()

## 바람의 흐름과 속도는 운항시간에 영향을 미치는 대표적인 요소로 볼 수 있음.

# EWR의 경우 다른 공항대비 높은 풍속을 가진것을 보여줌.

weather_EWR = flights_weather.loc[flights_weather["origin"] == "EWR", :]
weather_JFK = flights_weather.loc[flights_weather["origin"] == "JFK", :]
weather_LGA = flights_weather.loc[flights_weather["origin"] == "LGA", :]

## 공항에서 비행기 결항과 관련된 풍속은 평균 25KT이상, 최대 35KT이상인 경우를 뜻함.

sum(weather_EWR["wind_speed"] >= 35) # 60

sum(weather_JFK["wind_speed"] >= 35) # 97

sum(weather_LGA["wind_speed"] >= 35) # 23


## 공항에서 딜레이 시간의 비율
weather_EWR["arr_delay"].sort_values(ascending= False)
weather_EWR["wind_speed"].sort_values(ascending= False)

weather_EWR.iloc[8187,:] # EV
weather_EWR.iloc[86926,:] # EV
weather_EWR.iloc[194422,:] 
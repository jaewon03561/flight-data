import numpy as np
import pandas as pd

import os 
os.getcwd()
os.chdir("c:\\Users\\park\\Documents\\lsbigdata-gen4")
import pandas as pd



# 상자그림 1
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("./data/Obesity2.csv")
df.info()

plt.figure(figsize=(6,5))
sns.boxplot(x = df["NObeyesdad"],
            y = df["Weight"],
            palette= "Pastel1")
plt.xticks(rotation = 45)
plt.show()


# 상자 그림2
import pandas as pd
import matplotlib.pyplot as plt
df.boxplot(column= "Weight",
           by = "NObeyesdad",
           grid = False,
           figsize=(8,5))
plt.xlabel("Obesity Level")
plt.ylabel("Weight")
plt.title("Box Plot of Weight by Obesity2")
plt.suptitle("") # 자동 생성되는 그룹 제목 제거
plt.xticks(rotation=45)
plt.show()


df.boxplot(column = "Weight",
           by = "NObeyesdad",
           grid = False,
           figsize=(8,5))



plt.figure(figsize=(6,5))
plt.scatter(df["Height"], df["Weight"], alpha= 0.5)
plt.title("Scatter Plot of Height vs Weight")
plt.show()
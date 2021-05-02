"""Module that analyzes 'pripoy' crystallization """
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
temp_decr = []

df = pd.read_csv('temp_data.csv', sep=',') #Данные о охлаждении и кристаллизации припоя

for i in range(len(df)-1): #Изменения температуры <0.4 градусов считаем на плоскости кристаллизации
    delt = df.temp.iloc[i+1]-df.temp.iloc[i]
    if abs(delt) > 0.4:
        temp_decr.append(delt)
    else: pass

delta_temp = pd.DataFrame(data={'temp': temp_decr})

temps = delta_temp['temp']
print(stats.kstest(temps, 'norm')) #Не нормальное из-за P-value. Но лаба уже зачтена, так что...
delta_temp.plot.kde()
plt.show()

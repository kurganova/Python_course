# ДЗ
# Задача 1
# Определить среднюю стоимость дома
# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , 
# где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.

# import pandas as pd
# df = pd.read_csv('california_housing_train.csv')
# df = df.loc[df['population'] < 500,['median_house_value']]
# avg = df['median_house_value'].mean()
# # print(avg)


# Задача 2
# Максимальная households
# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального значения 
# переменной min_population и сохраните это значение в переменную max_households_in_min_population.
# Используйте модуль pandas.

# import pandas as pd
# df = pd.read_csv('california_housing_train.csv')
# min_population = df['population'].min()
# max_households_in_min_population = df[df['population'] == min_population].households.max()
# # print(max_households_in_min_population)
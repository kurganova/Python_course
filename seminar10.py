# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# Формат сдачи: ссылка на свой репозиторий.

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head(10)

# Перевод в one hot вид без get_dummies
pd.DataFrame({'human': data['whoAmI'] == 'human', 'robot': data['whoAmI'] == 'robot'}).astype(int).head(10)

# Перевод в one hot вид с get_dummies
pd.get_dummies(data['whoAmI']).astype(int).head(10)


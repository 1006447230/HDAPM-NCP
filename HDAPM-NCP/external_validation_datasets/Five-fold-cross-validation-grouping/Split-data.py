import pandas as pd
import random
import numpy as np

numbers1 = random.sample(range(1, 26), 5)
numbers1=np.array(numbers1)
np.savetxt("Random-number-1-1.txt", numbers1, fmt="%s", delimiter=',')
numbers2 = random.sample(range(1, 401), 80)
numbers2=np.array(numbers2)
np.savetxt("Random-number-1-2.txt", numbers2, fmt="%s", delimiter=',')
df_dis = pd.read_csv("disease.csv", header=None, names=['id', 'DiseaseId'])
df_herb = pd.read_csv(r"herb.csv", header=None, names=['id', 'HerbId'])
df_dis.set_index('DiseaseId', inplace=True)
df_herb.set_index('HerbId', inplace=True)
herb_disease_Data=np.loadtxt(r"disease-herb.txt", dtype=str,delimiter=',' )
contact_ratio = []

one=[]
Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0=[]
Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0=[]
Herbs_become_columns_of_0_and_diseases_become_rows_of_0=[]

for i in range(0,400):
    zero_matrix = []
    for i in range(0, 25):
        zero_matrix.append(0)
    contact_ratio.append(zero_matrix)


j=0
for data in herb_disease_Data:
    j=j+1
    row = int(df_dis.loc[data[0]].id)
    column = int(df_herb.loc[data[1]].id)
    if (column in numbers1) and (row in numbers2):
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    elif (column in numbers1) and (row not in numbers2) :
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0.append(data)
    elif (column not in numbers1) and (row in numbers2) :
        one.append(data)
        Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    else:
        contact_ratio[row - 1][column - 1] = 1

np.savetxt("1convert01.txt", one, fmt="%s", delimiter=',')
np.savetxt("1C.txt", Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("1B.txt", Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("1A.txt", Herbs_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-1.txt", contact_ratio, fmt="%s", delimiter=',')


existing_numbers = set()


with open('../five-cross-verification1/Random-number-1-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

random_numbers = []
while len(random_numbers) < 5:
    number = random.randint(1, 25)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)


np.savetxt("Random-number-2-1.txt", random_numbers, fmt="%s", delimiter=',')
numbers1 = random_numbers
existing_numbers2 = set()

with open('../five-cross-verification1/Random-number-1-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])


random_numbers2 = []
while len(random_numbers2) < 80:
    number2 = random.randint(1, 400)
    if number2 not in existing_numbers2 and number2 not in random_numbers2:
        random_numbers2.append(number2)
np.savetxt("Random-number-2-2.txt", random_numbers2, fmt="%s", delimiter=',')
numbers2 = random_numbers2
df_dis.set_index('DiseaseId', inplace=True)
df_herb.set_index('HerbId', inplace=True)
contact_ratio = []
one=[]
Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0=[]
Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0=[]
Herbs_become_columns_of_0_and_diseases_become_rows_of_0=[]
for i in range(0,400):
    zero_matrix = []
    for i in range(0, 25):
        zero_matrix.append(0)
    contact_ratio.append(zero_matrix)


j=0
for data in herb_disease_Data:
    j=j+1
    row = int(df_dis.loc[data[0]].id)
    column = int(df_herb.loc[data[1]].id)
    if (column in numbers1) and (row in numbers2):
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    elif (column in numbers1) and (row not in numbers2) :
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0.append(data)
    elif (column not in numbers1) and (row in numbers2) :
        one.append(data)
        Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    else:
        contact_ratio[row - 1][column - 1] = 1

np.savetxt("2convert01.txt", one, fmt="%s", delimiter=',')
np.savetxt("2C.txt", Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("2B.txt", Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("2A.txt", Herbs_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-2.txt", contact_ratio, fmt="%s", delimiter=',')




existing_numbers = set()


with open('../five-cross-verification1/Random-number-1-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

with open('../five-cross-verification2/Random-number-2-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


random_numbers = []
while len(random_numbers) < 5:
    number = random.randint(1, 25)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)


np.savetxt("Random-number-3-1.txt", random_numbers, fmt="%s", delimiter=',')
numbers1 = random_numbers



existing_numbers2 = set()

with open('../five-cross-verification1/Random-number-1-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])
with open('../five-cross-verification2/Random-number-2-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])


random_numbers2 = []
while len(random_numbers2) < 80:
    number2 = random.randint(1, 400)
    if number2 not in existing_numbers2 and number2 not in random_numbers2:
        random_numbers2.append(number2)



np.savetxt("Random-number-3-2.txt", random_numbers2, fmt="%s", delimiter=',')

numbers2 = random_numbers2

df_dis = pd.read_csv("E:\code_pycharm_project2023\herb_disease数据处理成矩阵\草药-疾病变成01向量\疾病（4000多条筛选后）（除去没有meshid）.csv", header=None, names=['id', 'DiseaseId'])
df_herb = pd.read_csv(r"E:\code_pycharm_project2023\herb_disease数据处理成矩阵\草药-疾病变成01向量\4000条去重后草药数据.csv", header=None, names=['id', 'HerbId'])

df_dis.set_index('DiseaseId', inplace=True)
df_herb.set_index('HerbId', inplace=True)

herb_disease_Data=np.loadtxt(r"E:\code_pycharm_project2023\herb_disease数据处理成矩阵\草药-疾病变成01向量\疾病-草药（4000多条对应）（除去没有meshid）.txt", dtype=str,delimiter=',' )

contact_ratio = []

one=[]
Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0=[]
Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0=[]
Herbs_become_columns_of_0_and_diseases_become_rows_of_0=[]

for i in range(0,400):
    zero_matrix = []
    for i in range(0, 25):
        zero_matrix.append(0)
    contact_ratio.append(zero_matrix)


j=0
for data in herb_disease_Data:
    j=j+1
    row = int(df_dis.loc[data[0]].id)
    column = int(df_herb.loc[data[1]].id)
    if (column in numbers1) and (row in numbers2):
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    elif (column in numbers1) and (row not in numbers2) :
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0.append(data)
    elif (column not in numbers1) and (row in numbers2) :
        one.append(data)
        Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    else:
        contact_ratio[row - 1][column - 1] = 1


np.savetxt("3convert01.txt", one, fmt="%s", delimiter=',')
np.savetxt("3C.txt", Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("3B.txt", Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("3A.txt", Herbs_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-3.txt", contact_ratio, fmt="%s", delimiter=',')



existing_numbers = set()

with open('../five-cross-verification1/Random-number-1-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])
with open('../five-cross-verification2/Random-number-2-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])
with open('../five-cross-verification3/Random-number-3-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

random_numbers = []
while len(random_numbers) < 5:
    number = random.randint(1, 25)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)


np.savetxt("Random-number-4-1.txt", random_numbers, fmt="%s", delimiter=',')

numbers1 = random_numbers





existing_numbers2 = set()

with open('../five-cross-verification1/Random-number-1-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])

with open('../five-cross-verification2/Random-number-2-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])

with open('../five-cross-verification3/Random-number-3-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])

random_numbers2 = []
while len(random_numbers2) < 80:
    number2 = random.randint(1, 400)
    if number2 not in existing_numbers2 and number2 not in random_numbers2:
        random_numbers2.append(number2)

np.savetxt("Random-number-4-2.txt", random_numbers2, fmt="%s", delimiter=',')
numbers2 = random_numbers2

contact_ratio = []

one=[]
Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0=[]
Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0=[]
Herbs_become_columns_of_0_and_diseases_become_rows_of_0=[]

for i in range(0,400):
    zero_matrix = []
    for i in range(0, 25):
        zero_matrix.append(0)
    contact_ratio.append(zero_matrix)
j=0
for data in herb_disease_Data:
    j=j+1
    row = int(df_dis.loc[data[0]].id)
    column = int(df_herb.loc[data[1]].id)
    if (column in numbers1) and (row in numbers2):
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    elif (column in numbers1) and (row not in numbers2) :
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0.append(data)
    elif (column not in numbers1) and (row in numbers2) :
        one.append(data)
        Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    else:
        contact_ratio[row - 1][column - 1] = 1


np.savetxt("4convert01.txt", one, fmt="%s", delimiter=',')
np.savetxt("4C.txt", Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("4B.txt", Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("4A.txt", Herbs_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-4.txt", contact_ratio, fmt="%s", delimiter=',')



existing_numbers = set()


with open('../five-cross-verification1/Random-number-1-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


with open('../five-cross-verification2/Random-number-2-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

with open('../five-cross-verification3/Random-number-3-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

with open('../five-cross-verification4/Random-number-4-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

random_numbers = []
while len(random_numbers) < 5:
    number = random.randint(1, 25)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)


np.savetxt("Random-number-5-1.txt", random_numbers, fmt="%s", delimiter=',')

numbers1 = random_numbers




existing_numbers2 = set()


with open('../five-cross-verification1/Random-number-1-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])

with open('../five-cross-verification2/Random-number-2-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])

with open('../five-cross-verification3/Random-number-3-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])

with open('../five-cross-verification4/Random-number-4-2.txt', 'r') as file:
    existing_numbers2.update([int(line.strip()) for line in file])

random_numbers2 = []
while len(random_numbers2) < 80:
    number2 = random.randint(1, 400)
    if number2 not in existing_numbers2 and number2 not in random_numbers2:
        random_numbers2.append(number2)


np.savetxt("Random-number-5-2.txt", random_numbers2, fmt="%s", delimiter=',')

numbers2 = random_numbers2


contact_ratio = []

one=[]
Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0=[]
Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0=[]
Herbs_become_columns_of_0_and_diseases_become_rows_of_0=[]

for i in range(0,400):
    zero_matrix = []
    for i in range(0, 25):
        zero_matrix.append(0)
    contact_ratio.append(zero_matrix)


j=0
for data in herb_disease_Data:
    j=j+1

    row = int(df_dis.loc[data[0]].id)

    column = int(df_herb.loc[data[1]].id)
    if (column in numbers1) and (row in numbers2):
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    elif (column in numbers1) and (row not in numbers2) :
        one.append(data)
        Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0.append(data)
    elif (column not in numbers1) and (row in numbers2) :

        one.append(data)
        Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0.append(data)
    else:

        contact_ratio[row - 1][column - 1] = 1


np.savetxt("5convert01.txt", one, fmt="%s", delimiter=',')
np.savetxt("5C.txt", Herbs_become_columns_of_0_and_diseases_do_not_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("5B.txt", Herbs_do_not_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("5A.txt", Herbs_become_columns_of_0_and_diseases_become_rows_of_0, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-5.txt", contact_ratio, fmt="%s", delimiter=',')


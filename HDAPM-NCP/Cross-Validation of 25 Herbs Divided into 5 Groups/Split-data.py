import pandas as pd
import random
import numpy as np

numbers1 = random.sample(range(1, 26), 5)
numbers1=np.array(numbers1)
np.savetxt("Random-number1.txt", numbers1, fmt="%s", delimiter=',')
df_dis = pd.read_csv("diseasedata.csv", header=None, names=['id', 'DiseaseId'])
df_herb = pd.read_csv(r"herbdata.csv", header=None, names=['id', 'HerbId'])
df_dis.set_index('DiseaseId', inplace=True)
df_herb.set_index('HerbId', inplace=True)
herb_disease_Data=np.loadtxt(r"herb-diseasedata.txt", dtype=str,delimiter=',' )
contact_ratio = []
one=[]
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
    if column in numbers1:
        one.append(data)
    if column not in numbers1:
        contact_ratio[row - 1][column - 1] = 1


np.savetxt("1convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("Herb-Disease-validation-1.txt", contact_ratio, fmt="%s", delimiter=',')


existing_numbers = set()


with open('Random-number1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

random_numbers = []
while len(random_numbers) < 5:
    number = random.randint(1, 25)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)
np.savetxt("Random-number2.txt", random_numbers, fmt="%s", delimiter=',')


numbers1 = random_numbers

one=[]

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
    if column in numbers1:
        one.append(data)
    if column not in numbers1:
        contact_ratio[row - 1][column - 1] = 1



np.savetxt("2convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("Herb-Disease-validation-2.txt", contact_ratio, fmt="%s", delimiter=',')




existing_numbers = set()


with open('Random-number1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


with open('Random-number2.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


random_numbers = []
while len(random_numbers) < 5:
    number = random.randint(1, 25)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)



np.savetxt("Random-number3.txt", random_numbers, fmt="%s", delimiter=',')

numbers1 = random_numbers



one=[]

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
    if column in numbers1:
        one.append(data)
    if column not in numbers1:
        contact_ratio[row - 1][column - 1] = 1

np.savetxt("3convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("Herb-Disease-validation-3.txt", contact_ratio, fmt="%s", delimiter=',')





existing_numbers = set()


with open('Random-number1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

with open('Random-number2.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


with open('Random-number3.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


random_numbers = []
while len(random_numbers) < 5:
    number = random.randint(1, 25)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)



np.savetxt("Random-number4.txt", random_numbers, fmt="%s", delimiter=',')

numbers1 = random_numbers



one=[]

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
    if column in numbers1:
        one.append(data)
    if column not in numbers1:
        contact_ratio[row - 1][column - 1] = 1


np.savetxt("4convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("Herb-Disease-validation-4.txt", contact_ratio, fmt="%s", delimiter=',')





existing_numbers = set()


with open('Random-number1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

with open('Random-number2.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

with open('Random-number3.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])
with open('Random-number4.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

random_numbers = []
while len(random_numbers) < 5:
    number = random.randint(1, 25)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)


np.savetxt("Random-number5.txt", random_numbers, fmt="%s", delimiter=',')
numbers1 = random_numbers



one=[]

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
    if column in numbers1:
        one.append(data)
    if column not in numbers1:
        contact_ratio[row - 1][column - 1] = 1

np.savetxt("5convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("Herb-Disease-validation-5.txt", contact_ratio, fmt="%s", delimiter=',')


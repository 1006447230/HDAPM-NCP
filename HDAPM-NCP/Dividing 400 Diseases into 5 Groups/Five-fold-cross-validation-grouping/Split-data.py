import pandas as pd
import random
import numpy as np

numbers1 = random.sample(range(1, 401), 80)
numbers1=np.array(numbers1)
np.savetxt("Random_number-1.txt", numbers1, fmt="%s", delimiter=',')
df_dis = pd.read_csv("diseasedata.csv", header=None, names=['id', 'DiseaseId'])
df_herb = pd.read_csv(r"herbdata.csv", header=None, names=['id', 'HerbId'])
df_dis.set_index('DiseaseId', inplace=True)
df_herb.set_index('HerbId', inplace=True)
herb_disease_Data=np.loadtxt(r"disease_herb.txt", dtype=str,delimiter=',' )
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
    if row in numbers1:

        one.append(data)
    if row not in numbers1:
        contact_ratio[row - 1][column - 1] = 1


np.savetxt("1convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-1.txt", contact_ratio, fmt="%s", delimiter=',')

existing_numbers = set()
with open('Random_number-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])
random_numbers = []
while len(random_numbers) < 80:
    number = random.randint(1, 400)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)
np.savetxt("Random_number-2.txt", random_numbers, fmt="%s", delimiter=',')
numbers1 = random_numbers




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
    if row in numbers1:

        one.append(data)
    if row not in numbers1:
        contact_ratio[row - 1][column - 1] = 1



np.savetxt("2convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-2.txt", contact_ratio, fmt="%s", delimiter=',')


existing_numbers = set()


with open('Random_number-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])
with open('andom_number-2.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


random_numbers = []
while len(random_numbers) < 80:
    number = random.randint(1, 400)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)

np.savetxt("Random_number-3.txt", random_numbers, fmt="%s", delimiter=',')
numbers1 = random_numbers




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
    if row in numbers1:
        one.append(data)
    if row not in numbers1:
        contact_ratio[row - 1][column - 1] = 1


np.savetxt("3convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-3.txt", contact_ratio, fmt="%s", delimiter=',')




existing_numbers = set()
with open('Random_number-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


with open('Random_number-2.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


with open('Random_number-3.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


random_numbers = []
while len(random_numbers) < 80:
    number = random.randint(1, 400)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)



np.savetxt("Random_number-4.txt", random_numbers, fmt="%s", delimiter=',')
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
    if row in numbers1:
        one.append(data)
    if row not in numbers1:
        contact_ratio[row - 1][column - 1] = 1


np.savetxt("4convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-4.txt", contact_ratio, fmt="%s", delimiter=',')


existing_numbers = set()


with open('Random_number-1.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


with open('Random_number-2.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])


with open('Random_number-3.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

with open('Random_number-4.txt', 'r') as file:
    existing_numbers.update([int(line.strip()) for line in file])

random_numbers = []
while len(random_numbers) < 80:
    number = random.randint(1, 400)
    if number not in existing_numbers and number not in random_numbers:
        random_numbers.append(number)



np.savetxt("Random_number-5.txt", random_numbers, fmt="%s", delimiter=',')



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
    if row in numbers1:
        one.append(data)
    if row not in numbers1:

        contact_ratio[row - 1][column - 1] = 1



np.savetxt("5convert0-1.txt", one, fmt="%s", delimiter=',')
np.savetxt("herb_disease01cross_verification-5.txt", contact_ratio, fmt="%s", delimiter=',')

